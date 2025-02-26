
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time

options = Options()
options.add_argument("--incognito")
options.add_argument("--disable-notifications")
options.add_argument("--disable-popup-blocking")
options.add_argument("--disable-features=NetworkService")

driver = webdriver.Chrome(options=options)

try:
    driver.get("https://practicetestautomation.com/")
    time.sleep(5)  # Wait for 5 seconds after opening the page

    driver.maximize_window()

    time.sleep(3)  # Wait for 3 seconds before every action

    # Find and click the "Home" menu
    home_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Home')]"))
    )
    home_link.click()

    time.sleep(3)  # Wait for 3 seconds after clicking

    # Verify the page URL
    current_url = driver.current_url
    assert current_url == "https://practicetestautomation.com/", "URL does not match"

    sys.exit(0)

except Exception as e:
    print("Test Failed: ", str(e))
    sys.exit(1)

finally:
    driver.quit()
