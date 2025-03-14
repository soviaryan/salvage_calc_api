from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def fetch_vehicle_info(lot_number):
    """
    Scrapes Copart for vehicle information using the given lot number.
    Returns a dictionary with vehicle details.
    """
    options = Options()
    options.add_argument("--headless")  # Run without UI
    options.add_argument("--no-sandbox")  # Bypass OS security model
    options.add_argument("--disable-dev-shm-usage")  # Overcome limited resources
    options.binary_location = "/usr/bin/google-chrome"  # Ensure it finds Chrome

    # Set up Chrome WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        url = f"https://www.copart.com/lot/{lot_number}"
        driver.get(url)

        # Allow page to load
        time.sleep(3)

        # Extract key details from Copart's page
        vehicle_data = {}
        vehicle_data["Lot Number"] = lot_number

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

        try:
            vehicle_data["Engine Type"] = driver.find_element(By.XPATH, "//span[contains(text(), 'Engine Type')]/following-sibling::span").text
        except:
            vehicle_data["Engine Type"] = "N/A"

        try:
            vehicle_data["Transmission"] = driver.find_element(By.XPATH, "//span[contains(text(), 'Transmission')]/following-sibling::span").text
        except:
            vehicle_data["Transmission"] = "N/A"

        try:
            vehicle_data["Drive"] = driver.find_element(By.XPATH, "//span[contains(text(), 'Drive')]/following-sibling::span").text
        except:
            vehicle_data["Drive"] = "N/A"

        try:
            vehicle_data["Fuel"] = driver.find_element(By.XPATH, "//span[contains(text(), 'Fuel')]/following-sibling::span").text
        except:
            vehicle_data["Fuel"] = "N/A"

        try:
            vehicle_data["Color"] = driver.find_element(By.XPATH, "//span[contains(text(), 'Color')]/following-sibling::span").text
        except:
            vehicle_data["Color"] = "N/A"

        try:
            vehicle_data["Keys Available"] = driver.find_element(By.XPATH, "//span[contains(text(), 'Keys Available')]/following-sibling::span").text
        except:
            vehicle_data["Keys Available"] = "N/A"

        return vehicle_data

    except Exception as e:
        return {"error": str(e)}

    finally:
        driver.quit()


