from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# --- Script to Save Page Source ---

def save_page_source(url, output_file):
    print("🚀 Starting browser to capture HTML source...")
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 20)
    
    try:
        driver.get(url)
        # Wait until the main data table is loaded and visible
        wait.until(EC.visibility_of_element_located((By.ID, "dataTablePS")))
        
        # Get the page source after JavaScript has loaded everything
        html_content = driver.page_source
        
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(html_content)
            
        print(f"✅ Successfully saved the page source to: {output_file}")
        
    except Exception as e:
        print(f"❌ An error occurred: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    target_url = "https://www.sih.gov.in/sih2025PS"
    save_page_source(target_url, "sih_page_source.html")