
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time

try:
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-features=NetworkService")

    driver = webdriver.Chrome(options=options)
    driver.get("https://practicetestautomation.com/practice-test-exceptions/")
    time.sleep(3)
    driver.maximize_window()

    add_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Add')]"))
    )
    time.sleep(3)
    add_button.click()

    confirmation_message = WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.ID, "confirmation"), "Row added successfully")
    )
    assert confirmation_message, "Expected message not found after adding row"

    input_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='row2']/input"))
    )
    time.sleep(3)
    input_field.send_keys("burger")

    save_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='save_btn']"))
    )
    time.sleep(3)
    save_button.click()

    confirmation_message = WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.ID, "confirmation"), "Row added successfully")
    )
    assert confirmation_message, "Expected message not found after saving row"

    remove_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='remove_btn']"))
    )
    time.sleep(3)
    remove_button.click()

    confirmation_message = WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.ID, "confirmation"), "Row 2 was removed")
    )
    assert confirmation_message, "Expected message not found after removing row"

    print("Test passed.")
    sys.exit(0)

except Exception as e:
    print("Test failed:", str(e))
    sys.exit(1)

finally:
    driver.quit()
