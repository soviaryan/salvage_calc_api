from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def fetch_vehicle_info(lot_number):
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run without UI
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.binary_location = "/usr/bin/google-chrome-stable"  # Explicitly set the path

    service = Service("/usr/bin/chromedriver")  # Ensure we use the installed ChromeDriver
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



