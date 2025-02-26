
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

def test_scenario():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--incognito')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-features=NetworkService')
    options.add_argument('--disable-notifications')

    driver = webdriver.Chrome(options=options)
    driver.get("https://practicetestautomation.com/practice-test-exceptions/")
    driver.maximize_window()
    time.sleep(5)

    try:
        add_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Add')]"))
        )
        time.sleep(3)
        add_button.click()

        confirmation = WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.XPATH, "//*[@id='confirmation']"), "Row added successfully")
        )
        if not confirmation:
            raise Exception("Add confirmation message not found")

        input_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='row2']/input"))
        )
        time.sleep(3)
        input_field.send_keys("burger")

        save_btn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='save_btn']"))
        )
        time.sleep(3)
        save_btn.click()

        confirmation = WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.XPATH, "//*[@id='confirmation']"), "Row added successfully")
        )
        if not confirmation:
            raise Exception("Save confirmation message not found")

        remove_btn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='remove_btn']"))
        )
        time.sleep(3)
        remove_btn.click()

        confirmation = WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.XPATH, "//*[@id='confirmation']"), "Row 2 was removed")
        )
        if not confirmation:
            raise Exception("Remove confirmation message not found")

        sys.exit(0)
    
    except Exception as e:
        print(f"Test failed: {e}")
        sys.exit(1)
    
    finally:
        driver.quit()

if __name__ == "__main__":
    test_scenario()
