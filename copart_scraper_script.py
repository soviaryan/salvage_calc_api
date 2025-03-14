from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os
import time

def fetch_vehicle_info(lot_number):
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run without UI
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Manually set Chrome and ChromeDriver paths
    chrome_binary_path = os.environ.get("CHROME_BIN", "/usr/bin/google-chrome")
    chromedriver_path = os.environ.get("CHROMEDRIVER_BIN", "/usr/bin/chromedriver")

    # Ensure paths are correct
    if not os.path.exists(chrome_binary_path):
        return {"error": "Chrome binary not found!"}
    if not os.path.exists(chromedriver_path):
        return {"error": "ChromeDriver binary not found!"}

    chrome_options.binary_location = chrome_binary_path
    service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        url = f"https://www.copart.com/lot/{lot_number}"
        driver.get(url)
        time.sleep(3)  # Allow page to load

        vehicle_data = {"Lot Number": lot_number}

        try:
            vehicle_data["Title"] = driver.find_element(By.XPATH, "//span[contains(text(), 'Title')]/following-sibling::span").text
        except:
            vehicle_data["Title"] = "N/A"

        try:
            vehicle_data["Odometer"] = driver.find_element(By.XPATH, "//span[contains(text(), 'Odometer')]/following-sibling::span").text
        except:
            vehicle_data["Odometer"] = "N/A"

        return vehicle_data

    except Exception as e:
        return {"error": str(e)}

    finally:
        driver.quit()



