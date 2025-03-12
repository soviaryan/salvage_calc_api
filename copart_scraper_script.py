from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def fetch_vehicle_info(lot_number):
    url = f"https://www.copart.com/lot/{lot_number}"
    print(f"🔄 Fetching: {url}")

    # Set up Chrome options for headless mode (faster)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Set up WebDriver
    service = Service("chromedriver.exe")  # Ensure chromedriver.exe is in the same folder
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.get(url)
        time.sleep(5)  # Wait for page to load

        # Extract data from Copart page
        vehicle_data = {
            "Lot Number": lot_number,
            "VIN": "Not Found",
            "Title": "Not Found",
            "Odometer": "Not Found",
            "Primary Damage": "Not Found",
            "Estimated Retail Value": "Not Found",
            "Cylinders": "Not Found",
            "Color": "Not Found",
            "Engine Type": "Not Found",
            "Transmission": "Not Found",
            "Drive": "Not Found",
            "Vehicle Type": "Not Found",
            "Fuel": "Not Found",
            "Keys Available": "Not Found"
        }

        # Extract vehicle details
        span_elements = driver.find_elements(By.CLASS_NAME, "lot-details-desc")

        if span_elements:
            extracted_values = [span.text.strip() for span in span_elements if span.text.strip()]
            print(f"🔍 DEBUG: Found span elements:\n{extracted_values}")

            # Map extracted values to vehicle data fields
            if len(extracted_values) >= 14:
                vehicle_data.update({
                    "VIN": extracted_values[1],
                    "Title": extracted_values[2],
                    "Odometer": extracted_values[3],
                    "Primary Damage": extracted_values[4],
                    "Estimated Retail Value": extracted_values[5],
                    "Cylinders": extracted_values[6],
                    "Color": extracted_values[7],
                    "Engine Type": extracted_values[8],
                    "Transmission": extracted_values[9],
                    "Drive": extracted_values[10],
                    "Vehicle Type": extracted_values[11],
                    "Fuel": extracted_values[12],
                    "Keys Available": extracted_values[13]
                })

        print(f"✅ Extracted Data: {vehicle_data}")
        return vehicle_data

    except Exception as e:
        print(f"❌ Error: {e}")
        return {"error": "Failed to fetch vehicle info"}

    finally:
        driver.quit()

# Run this script directly to test scraping a specific lot number
if __name__ == "__main__":
    test_lot = "41344685"
    fetch_vehicle_info(test_lot)

