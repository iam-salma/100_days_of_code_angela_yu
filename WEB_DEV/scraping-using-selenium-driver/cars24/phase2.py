import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# ----------------------------
# Load car links from CSV
# ----------------------------
links_df = pd.read_csv("tata_cars_mumbai_links.csv")
car_links = links_df["URL"].dropna().tolist()
print(f"Loaded {len(car_links)} links from tata_cars_mumbai_links.csv")

# ----------------------------
# Setup Selenium
# ----------------------------
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 15)

# ----------------------------
# Extract details from each car page
# ----------------------------
data = []

for idx, link in enumerate(car_links, start=1):
    try:
        driver.get(link)
        print(f"[{idx}/{len(car_links)}] Scraping: {link}")

        # Title (Year, Title, Variant)
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

        # Location
        try:
            location = wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, "div.styles_hubLocation__AOuo3 p"))
            ).text.strip()
        except:
            location = "N/A"

        # Price
        try:
            price = wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, "div.styles_price__3yE9i p"))
            ).text.strip()
        except:
            price = "N/A"

        # Meta Info (KM, Owners, Transmission, Fuel)
        km = owners = transmission = fuel = "N/A"
        try:
            meta_blocks = driver.find_elements(By.CSS_SELECTOR, "p.sc-braxZu.kvfdZL")
            for block in meta_blocks:
                text = block.text.strip().lower()
                if "km" in text:
                    km = block.text.strip()
                elif "owner" in text:
                    owners = block.text.strip()
                elif "manual" in text or "automatic" in text:
                    transmission = block.text.strip()
                elif any(fuel_type in text for fuel_type in ["petrol", "diesel", "cng", "electric"]):
                    fuel = block.text.strip()
        except:
            pass

        # Append row
        data.append({
            "Title": title,
            "Variant": variant,
            "Kilometers Driven": km,
            "Year of Manufacture": year,
            "Fuel Type": fuel,
            "Transmission": transmission,
            "Price": price,
            "Location": location,
            "Number of Owners": owners,
            "URL": link
        })

    except Exception as e:
        print(f"❌ Error scraping {link}: {e}")

# ----------------------------
# Save results to Excel
# ----------------------------
df = pd.DataFrame(data)
excel_filename = "tata_cars_mumbai_details.xlsx"
df.to_excel(excel_filename, index=False, engine="openpyxl")
print(f"✅ Data saved to {excel_filename}")

driver.quit()
