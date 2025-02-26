
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import sys
import time

chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-features=NetworkService")

driver = webdriver.Chrome(options=chrome_options)

try:
    driver.get("https://practicetestautomation.com/practice-test-login/")
    time.sleep(3)
    driver.maximize_window()

    # Wait for the username field
    username_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@name='username']"))
    )
    time.sleep(3)
    username_field.send_keys("student")

    # Wait for the password field
    password_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@name='password']"))
    )
    time.sleep(3)
    password_field.send_keys("Password123")

    # Wait for the submit button
    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='submit']"))
    )
    time.sleep(3)
    submit_button.click()

    # Verify successful login by checking element on the landing page
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Logout')]"))
    )

    print("Test Passed")
    sys.exit(0)

except Exception as e:
    print(f"Test Failed: {e}")
    sys.exit(1)

finally:
    driver.quit()
