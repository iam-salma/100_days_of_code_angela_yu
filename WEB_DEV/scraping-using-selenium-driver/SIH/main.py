import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# No changes needed to safe_click, it's already robust.
def safe_click(driver, element):
    try:
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        time.sleep(0.5)
        element.click()
    except Exception:
        try:
            from selenium.webdriver.common.action_chains import ActionChains
            ActionChains(driver).move_to_element(element).click().perform()
        except Exception:
            driver.execute_script("arguments[0].click();", element)

# --- COMPLETELY REWRITTEN FOR STABILITY ---
def scrape_page(driver, wait):
    page_data = []
    problem_ids = []
    record = {}
    
    try:
        # Step 1: Find all links and extract their unique data-target IDs.
        # This list of strings is stable and won't become "stale".
        links = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#dataTablePS tbody tr a")))
        for link in links:
            target_id = link.get_attribute('data-target')
            if target_id:
                # Extracts '#ViewProblemStatement25001'
                problem_ids.append(target_id)
    except TimeoutException:
        print("Could not find any problem statement links on this page.")
        return []

    # Step 2: Loop through the list of stable IDs, not a list of elements.
    for i, p_id in enumerate(problem_ids):
        try:
            # Step 3: Find the specific link fresh every single time using its unique ID.
            # This is the key to defeating the stale element error.
            link_selector = f"a[data-target='{p_id}']"
            link_to_click = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, link_selector)))
            
            safe_click(driver, link_to_click)

            # Wait for the modal to be visible and scrape it
            modal_selector = f"div{p_id}.modal"
            modal = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, modal_selector)))

            rows_modal = modal.find_elements(By.CSS_SELECTOR, "table#settings tr")
            for r in rows_modal:
                try:
                    key = r.find_element(By.TAG_NAME, "th").text.strip()
                    val = r.find_element(By.TAG_NAME, "td").text.strip()
                    if key:
                        record[key] = val
                except NoSuchElementException:
                    continue
            
            # --- THIS IS THE FIX ---
            table_row = link_to_click.find_element(By.XPATH, "./ancestor::tr")
            columns = table_row.find_elements(By.TAG_NAME, "td")
            
            # Switched from .text to .get_attribute('textContent') for reliability
            if len(columns) > 3:
                record["Submitted ideas Count"] = columns[3].get_attribute('textContent').strip()
            if len(columns) > 4:
                record["Deadline for idea submission"] = columns[4].get_attribute('textContent').strip()
            
            page_data.append(record)
            print(f"✔ Scraped ID {record.get('Problem Statement ID','N/A')} (row {i+1}/{len(problem_ids)})")

            # Close the modal and wait for it to disappear
            close_btn = modal.find_element(By.CSS_SELECTOR, "button.close.PSclose")
            driver.execute_script("arguments[0].click();", close_btn)
            wait.until(EC.invisibility_of_element(modal))

        except Exception as e:
            print(f"❌ Error on row {i+1} (ID: {p_id}): {e}")
            
            continue # Try to continue with the next item
            
    return page_data

def scrape_all_pages(driver, wait):
    all_data = []
    page = 1
    while True:
        print(f"\n📄 Scraping page {page}...")
        all_data.extend(scrape_page(driver, wait))
        
        try:
            first_row = driver.find_element(By.CSS_SELECTOR, "#dataTablePS tbody tr")
            next_li = driver.find_element(By.ID, "dataTablePS_next")
            
            if "disabled" in (next_li.get_attribute("class") or ""):
                print("\n✅ Reached the last page.")
                break
            
            next_button_link = next_li.find_element(By.TAG_NAME, "a")
            safe_click(driver, next_button_link)
            
            wait.until(EC.staleness_of(first_row))
            page += 1
            
        except Exception as e:
            print(f"\n⚠️ Pagination stopped unexpectedly: {e}")
            break
            
    return all_data

def main():
    options = webdriver.ChromeOptions()
    arguments = [
        "--disable-gpu", "--window-size=1920,1080",
        "--no-sandbox", "--disable-dev-shm-usage", "--blink-settings=imagesEnabled=false"
    ]
    for arg in arguments:
        options.add_argument(arg)
    options.add_experimental_option('excludeSwitches', ['enable-logging', 'enable-automation'])
    
    service = ChromeService()
    driver = webdriver.Chrome(service=service, options=options)
    
    try:
        wait = WebDriverWait(driver, 15)
        driver.get("https://www.sih.gov.in/sih2025PS")
        print("🚀 Starting scrape...\n")
        data = scrape_all_pages(driver, wait)

        if data:
            df = pd.DataFrame(data)
            df.to_excel("sih_problem_statements.xlsx", index=False)
            print(f"\n📊 Saved {len(df)} problem statements to sih_problem_statements.xlsx")
        else:
            print("\n🤷 No data was scraped.")
    finally:
        print("\n🔒 Scraping finished. Closing driver.")
        driver.quit()

if __name__ == "__main__":
    main()