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

# first lets set up the selenium driver !
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 15)


# to count the number of loaded car cards
def get_car_elements(driver):
    selectors = [
        "a.styles_carCardWrapper__sXLIp",
        "a[class*='carCard']",
        "a[href*='/cars/']",
        "a[href*='/buy-used-cars-']"
    ]
    for sel in selectors:
        els = driver.find_elements(By.CSS_SELECTOR, sel)
        if els:
            return els
    return []


# automate scroll and collect links
def scroll_and_collect_links(city_url):
    driver.get(city_url)
    time.sleep(2)
    
    max_scroll_cycles = 100
    no_change_limit = 6
    
    prev_count = 0
    no_change_count = 0
    cycle = 0

    while cycle < max_scroll_cycles and no_change_count < no_change_limit:
        cycle += 1
        cards = get_car_elements(driver)
        current_count = len(cards)
        print(f"[{cycle}] current card count: {current_count}")

        if current_count > prev_count:
            no_change_count = 0
            prev_count = current_count
        else:
            no_change_count += 1

        if cards:
            last = cards[-1]
            try:
                driver.execute_script("arguments[0].scrollIntoView({behavior:'auto', block:'end'});", last)
            except StaleElementReferenceException:
                pass
        else:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        time.sleep(1.2)

    car_elements = get_car_elements(driver)
    links = [a.get_attribute("href") for a in car_elements if a.get_attribute("href")]
    
    return list(dict.fromkeys(links))


# extract car details from each link
def scrape_car_details(car_links, city):
    data = []
    for idx, link in enumerate(car_links, start=1):
        try:
            driver.get(link)
            print(f"[{idx}/{len(car_links)}] Scraping: {link}")

            try:
                title_block = wait.until(EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "div.styles_carName__xzcd4 h1"))
                ).text.strip()
            except:
                title_block = "N/A"

            parts = title_block.split()
            year = parts[0] if parts and parts[0].isdigit() else "N/A"
            title = " ".join(parts[1:3]) if len(parts) > 2 else "N/A"
            variant = " ".join(parts[3:]) if len(parts) > 3 else "N/A"

            try:
                price = int(wait.until(EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "div.styles_price__3yE9i p"))
                ).text.replace("₹", "").replace(".", "").replace(" lakh", "000").strip())
            except:
                price = "N/A"
                
            try:
                location = wait.until(EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "div.styles_hubLocation__AOuo3 p"))
                ).text.strip()
            except:
                location = "N/A"
            
            km = owners = transmission = fuel = "N/A"
            try:
                meta_blocks = driver.find_elements(By.CSS_SELECTOR, "p.sc-braxZu.kvfdZL")
                for block in meta_blocks:
                    text = block.text.strip().lower()
                    if "km" in text:
                        km = block.text.replace("km", "").replace(".",",").replace("k", "0").replace("L", "0,000").strip()
                    elif "owner" in text:
                        owners = int(block.text.replace("owner", "").replace("st", "").replace("nd", "").replace("rd", "").strip())
                    elif "manual" in text or "automatic" in text:
                        transmission = block.text.strip()
                    elif any(fuel_type in text for fuel_type in ["petrol", "diesel", "cng", "electric"]):
                        fuel = block.text.strip()
            except:
                pass
                
            if title == "N/A":
                continue
            
            data.append({
                "City": city,
                "Model": title,
                "Variant": variant,
                "Kilometers Driven": km,
                "Year of Manufacture": year,
                "Fuel Type": fuel,
                "Transmission": transmission,
                "Price": price,
                "Location": location,
                "Number of Owners": owners,
            })

        except Exception as e:
            print(f"Error scraping {link}: {e}")
            continue
        
    return data


# lets start find tata cars in Mumbai, Hyderabad and New Delhi :)
cities = {
    "Mumbai": "https://www.cars24.com/buy-used-tata-cars-mumbai/?sort=bestmatch&serveWarrantyCount=true&storeCityId=2378",
    "Hyderabad": "https://www.cars24.com/buy-used-tata-cars-hyderabad/?sort=bestmatch&serveWarrantyCount=true&storeCityId=1706",
    "New Delhi": "https://www.cars24.com/buy-used-tata-cars-new-delhi/?sort=bestmatch&serveWarrantyCount=true&storeCityId=1452"
}


all_data = []
for city in cities:
    print(f"\nCollecting car links for {city}")
    car_links = scroll_and_collect_links(cities[city])
    print(f"Found {len(car_links)} links for {city}")
    details = scrape_car_details(car_links, city)
    
    # # Save each city details to separate Excel files
    # df = pd.DataFrame(details)
    # df.to_excel(f"tata_cars_{city.lower().replace(' ', '_')}_details.xlsx", index=False, engine="openpyxl")
    # print(f"Data saved for {city}")

    all_data.extend(details)


# Save to Excel
df = pd.DataFrame(all_data)
df.to_excel(f"tata_cars_in_multiple_cities.xlsx", index=False, engine="openpyxl")
print(f"Data saved")

driver.quit()
