import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def fetch_vehicle_info(lot_number):
    # Set Chrome and ChromeDriver paths
    chrome_binary_path = os.environ.get("GOOGLE_CHROME_BIN", "/usr/bin/google-chrome")
    chromedriver_path = os.environ.get("CHROMEDRIVER_PATH", "/usr/local/bin/chromedriver")

    # Ensure paths are valid
    if not os.path.exists(chrome_binary_path):
        return {"error": "Chrome binary not found!"}
    if not os.path.exists(chromedriver_path):
        return {"error": "ChromeDriver binary not found!"}

    # Configure Chrome options
    chrome_options = Options()
    chrome_options.binary_location = chrome_binary_path
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    try:
        # Launch browser
        driver = webdriver.Chrome(executable_path=chromedriver_path, options=chrome_options)

        # Go to Copart page
        url = f"https://www.copart.com/lot/{lot_number}"
        driver.get(url)

        time.sleep(3)  # Wait for content to load — ideally replace with WebDriverWait

        # Example: Try to extract vehicle title and location
        vehicle_title = driver.find_element(By.CLASS_NAME, "lot-title").text
        location = driver.find_element(By.CLASS_NAME, "location-information").text

        driver.quit()

        return {
            "lot_number": lot_number,
            "vehicle_title": vehicle_title,
            "location": location
        }

    except Exception as e:
        return {"error": str(e)}




