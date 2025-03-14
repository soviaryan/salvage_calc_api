from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

def fetch_vehicle_info(lot_number):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.binary_location = "/usr/bin/google-chrome"

    # Manually specify ChromeDriver path
    chromedriver_path = "/usr/local/bin/chromedriver"
    service = Service(chromedriver_path)

    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        url = f"https://www.copart.com/lot/{lot_number}"
        driver.get(url)
        time.sleep(3)

        vehicle_data = {"Lot Number": lot_number}

        # Extract details
        try:
            vehicle_data["Title"] = driver.find_element(By.XPATH, "//span[contains(text(), 'Title')]/following-sibling::span").text
        except:
            vehicle_data["Title"] = "N/A"

        try:
            vehicle_data["Odometer"] = driver.find_element(By.XPATH, "//span[contains(text(), 'Odometer')]/following-sibling::span").text
        except:
            vehicle_data["Odometer"] = "N/A"

        try:
            vehicle_data["Primary Damage"] = driver.find_element(By.XPATH, "//span[contains(text(), 'Primary Damage')]/following-sibling::span").text
        except:
            vehicle_data["Primary Damage"] = "N/A"

        try:
            vehicle_data["Estimated Retail Value"] = driver.find_element(By.XPATH, "//span[contains(text(), 'Estimated Retail Value')]/following-sibling::span").text
        except:
            vehicle_data["Estimated Retail Value"] = "N/A"

        return vehicle_data

    except Exception as e:
        return {"error": str(e)}

    finally:
        driver.quit()

