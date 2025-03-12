import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def fetch_vehicle_info(lot_number):
    """
    Fetches vehicle details from Copart using Selenium and Chrome in headless mode.
    
    Args:
        lot_number (str): The Copart lot number to search for.
    
    Returns:
        dict: Extracted vehicle details or an error message if the process fails.
    """
    url = f"https://www.copart.com/lot/{lot_number}"

    # Configure Chrome to run in headless mode on a server (Render)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")  # No UI
    chrome_options.add_argument("--no-sandbox")  # Required for running in containers
    chrome_options.add_argument("--disable-dev-shm-usage")  # Prevent memory issues
    chrome_options.add_argument("--disable-gpu")  # Disable GPU hardware acceleration
    chrome_options.add_argument("--remote-debugging-port=9222")  # Enable debugging

    # Start WebDriver with Chrome
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        print(f"🔄 Fetching: {url}")
        driver.get(url)
        time.sleep(3)  # Wait for page to load

        # Extract vehicle details
        span_elements = driver.find_elements(By.TAG_NAME, "span")
        span_texts = [elem.text.strip() for elem in span_elements if elem.text.strip()]

        if len(span_texts) < 15:
            print("❌ Failed to extract vehicle data.")
            return {"detail": "Not Found"}

        vehicle_data = {
            "Lot Number": span_texts[0],
            "VIN": span_texts[1],
            "Title": span_texts[2],
            "Odometer": span_texts[3],
            "Primary Damage": span_texts[4],
            "Estimated Retail Value": span_texts[5],
            "Cylinders": span_texts[6],
            "Color": span_texts[7],
            "Engine Type": span_texts[8],
            "Transmission": span_texts[9],
            "Drive": span_texts[10],
            "Vehicle Type": span_texts[11],
            "Fuel": span_texts[12],
            "Keys Available": span_texts[13]
        }

        print(f"✅ Extracted Data: {vehicle_data}")
        return vehicle_data

    except Exception as e:
        print(f"❌ Error occurred: {e}")
        return {"detail": "Scraper Failed", "error": str(e)}

    finally:
        driver.quit()  # Ensure the driver is closed properly

