from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import traceback
import time
import os

def fetch_vehicle_info(lot_number):
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Runs Chrome in headless mode
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # ✅ Dynamically find Chrome binary path
    chrome_path = os.getenv("GOOGLE_CHROME_BIN", "/usr/bin/google-chrome")
    chrome_options.binary_location = chrome_path

    # ✅ Use system-installed ChromeDriver
    chromedriver_path = "/usr/local/bin/chromedriver"
    service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        url = f"https://www.copart.com/lot/{lot_number}"
        print(f"🔍 Fetching data for {url}")
        driver.get(url)

        # ✅ Use WebDriverWait instead of fixed sleep
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        vehicle_data = {"Lot Number": lot_number}

        def get_text(xpath, default="N/A"):
            try:
                return driver.find_element(By.XPATH, xpath).text.strip()
            except:
                return default

        # ✅ Optimized data extraction
        vehicle_data["Title"] = get_text("//span[contains(text(), 'Title')]/following-sibling::span")
        vehicle_data["Odometer"] = get_text("//span[contains(text(), 'Odometer')]/following-sibling::span")
        vehicle_data["Primary Damage"] = get_text("//span[contains(text(), 'Primary Damage')]/following-sibling::span")
        vehicle_data["Estimated Retail Value"] = get_text("//span[contains(text(), 'Estimated Retail Value')]/following-sibling::span")
        vehicle_data["Engine Type"] = get_text("//span[contains(text(), 'Engine Type')]/following-sibling::span")
        vehicle_data["Transmission"] = get_text("//span[contains(text(), 'Transmission')]/following-sibling::span")
        vehicle_data["Drive"] = get_text("//span[contains(text(), 'Drive')]/following-sibling::span")
        vehicle_data["Fuel"] = get_text("//span[contains(text(), 'Fuel')]/following-sibling::span")
        vehicle_data["Color"] = get_text("//span[contains(text(), 'Color')]/following-sibling::span")
        vehicle_data["Keys Available"] = get_text("//span[contains(text(), 'Keys Available')]/following-sibling::span")

        return vehicle_data

    except Exception as e:
        print("❌ Error:", traceback.format_exc())  # ✅ Logs full error
        return {"error": str(e)}

    finally:
        driver.quit()
