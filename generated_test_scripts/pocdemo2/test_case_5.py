
import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_ui():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--disable-features=NetworkService")

    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.maximize_window()
        driver.get("https://practicetestautomation.com/")
        time.sleep(3)

        wait = WebDriverWait(driver, 10)
        
        # Waiting for the "Practice" menu to be visible and clickable
        practice_menu = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Practice')]")))
        time.sleep(3)
        practice_menu.click()
        time.sleep(3)
        
        # Verifying that the URL is correct
        wait.until(EC.url_to_be("https://practicetestautomation.com/practice/"))

        sys.exit(0)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
    finally:
        driver.quit()

if __name__ == "__main__":
    test_ui()
