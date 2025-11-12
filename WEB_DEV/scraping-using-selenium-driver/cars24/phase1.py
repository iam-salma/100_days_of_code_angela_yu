import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from webdriver_manager.chrome import ChromeDriverManager

# ----------------------------
# Setup Selenium
# ----------------------------
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
# if you previously used headless, try non-headless (headful)
# options.add_argument("--headless=new")  # DON'T use headless while debugging
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 15)

# ----------------------------
# Helpers
# ----------------------------
def accept_cookies_if_any(driver):
    try:
        # common patterns for cookie/consent
        possible_buttons = driver.find_elements(By.XPATH,
            "//button[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'accept') or "
            "contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'agree') or "
            "contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'got it') or "
            "contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'ok')]")
        for b in possible_buttons:
            try:
                if b.is_displayed():
                    driver.execute_script("arguments[0].click();", b)
                    print("Clicked cookie/consent button")
                    time.sleep(1)
                    return
            except Exception:
                continue
    except Exception:
        pass

def get_car_elements(driver):
    # Try a few selectors; site classnames may change so these are fallbacks.
    selectors = [
        "a.styles_carCardWrapper__sXLIp",     # original
        "a[class*='carCard']",                # fallback
        "a[href*='/cars/']",                  # generic car hrefs
        "a[href*='/buy-used-cars-']"
    ]
    for sel in selectors:
        els = driver.find_elements(By.CSS_SELECTOR, sel)
        if els:
            return els
    return []

def click_load_more_if_present(driver):
    try:
        # common text on load more buttons
        btn = driver.find_element(By.XPATH,
            "//button[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'load more') or "
            "contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'show more') or "
            "contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'view more')]")
        if btn.is_displayed():
            driver.execute_script("arguments[0].click();", btn)
            print("Clicked 'Load more' button")
            time.sleep(2)
            return True
    except Exception:
        return False

# ----------------------------
# Step 1: Go to Tata cars in Mumbai
# ----------------------------
url = "https://www.cars24.com/buy-used-cars-mumbai/?brand=Tata"
driver.get(url)
time.sleep(2)

# dismiss cookie/consent if present
accept_cookies_if_any(driver)

# ----------------------------
# Step 2: Robust scroll-to-load loop
# ----------------------------
max_scroll_cycles = 120
no_change_limit = 8
prev_count = 0
no_change_count = 0
cycle = 0

print("Starting robust scroll loop...")

while cycle < max_scroll_cycles and no_change_count < no_change_limit:
    cycle += 1
    cards = get_car_elements(driver)
    current_count = len(cards)
    print(f"[cycle {cycle}] current card count: {current_count} (prev {prev_count})")

    # If more cards loaded, reset the no_change counter
    if current_count > prev_count:
        no_change_count = 0
        prev_count = current_count
    else:
        no_change_count += 1

    # Try clicking a 'load more' button if present
    clicked = click_load_more_if_present(driver)
    if clicked:
        # wait briefly for new cards
        try:
            WebDriverWait(driver, 8).until(
                lambda d: len(get_car_elements(d)) > current_count
            )
            print("New cards detected after clicking load more.")
            prev_count = len(get_car_elements(driver))
            no_change_count = 0
            continue
        except TimeoutException:
            print("No new cards after clicking load more.")

    # Scroll the last card into view (best for IntersectionObserver)
    if cards:
        last = cards[-1]
        try:
            driver.execute_script("arguments[0].scrollIntoView({behavior:'auto', block:'end', inline:'nearest'});", last)
        except StaleElementReferenceException:
            pass
    else:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Send several page-downs as a fallback
    try:
        body = driver.find_element(By.TAG_NAME, "body")
        for _ in range(3):
            body.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.2)
    except Exception:
        driver.execute_script("window.scrollBy(0, window.innerHeight);")

    # Wait a moment for AJAX to fetch more cards, but also wait explicitly for more elements when possible
    try:
        WebDriverWait(driver, 6).until(lambda d: len(get_car_elements(d)) > current_count)
        print("Detected new cards via explicit wait.")
        prev_count = len(get_car_elements(driver))
        no_change_count = 0
        continue
    except TimeoutException:
        # no new cards within the wait window; continue loop and try again
        pass

    # small pause before next cycle
    time.sleep(1.2)

print(f"Finished scrolling. total cycles: {cycle}. final card count: {prev_count}")

# ----------------------------
# Step 3: Collect all car links (deduplicated)
# ----------------------------
car_elements = get_car_elements(driver)
links = []
for a in car_elements:
    try:
        href = a.get_attribute("href")
        if href:
            links.append(href)
    except Exception:
        continue

unique_links = list(dict.fromkeys(links))  # preserve order, dedupe
print(f"Found {len(unique_links)} unique car links")

# Quick sample print
for i, link in enumerate(unique_links[:10], 1):
    print(f"{i}. {link}")

# ----------------------------
# Step 4: (Optional) scrape each car page - similar to your original loop
# ----------------------------
# ... your scraping loop here ...

# Save to csv (example)
df = pd.DataFrame({"URL": unique_links})
df.to_csv("tata_cars_mumbai_links.csv", index=False)
print("Saved links to tata_cars_mumbai_links.csv")

driver.quit()
