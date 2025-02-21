
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

def configure_browser():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-features=NetworkService")
    return chrome_options

def test_remove_row():
    passed = False
    try:
        driver = webdriver.Chrome(options=configure_browser())

        driver.get("http://yourwebsite.com/test-exceptions") 
        driver.maximize_window()
        time.sleep(5)

        wait = WebDriverWait(driver, 10)

        # Add a row
        add_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Add Row')]")))
        time.sleep(3)
        add_button.click()

        # Enter "burger" in the row
        input_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='new_row_input']")))
        time.sleep(3)
        input_field.send_keys("burger")

        # Click remove button
        remove_button = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='remove_btn']")))
        time.sleep(3)
        remove_button.click()

        # Verify message
        message = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Row 2 was removed')]")))
        time.sleep(3)

        if message.text == "Row removed successfully":
            passed = True

    except Exception as e:
        print(e)
    finally:
        driver.quit()
        if passed:
            sys.exit(0)
        else:
            sys.exit(1)

if __name__ == "__main__":
    test_remove_row()
