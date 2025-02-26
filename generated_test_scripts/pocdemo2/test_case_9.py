
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

try:
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-features=NetworkService")

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    driver.get("https://practicetestautomation.com/practice-test-exceptions/")
    time.sleep(3)

    add_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Add')]"))
    )
    time.sleep(3)
    add_button.click()

    confirmation_msg = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='confirmation']"))
    )

    if "Row added successfully" not in confirmation_msg.text:
        raise Exception("Row added confirmation message not found.")

    new_row_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='row2']/input"))
    )
    time.sleep(3)
    new_row_input.send_keys("burger")

    save_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='save_btn']"))
    )
    time.sleep(3)
    save_button.click()

    confirmation_msg = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='confirmation']"))
    )

    if "Row added successfully" not in confirmation_msg.text:
        raise Exception("Row added confirmation message not found after saving.")

    sys.exit(0)

except Exception as e:
    print(e)
    sys.exit(1)

finally:
    driver.quit()
