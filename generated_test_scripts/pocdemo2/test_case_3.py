
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")
options.add_argument("--disable-popups")
options.add_argument("--incognito")
options.add_argument("--disable-features=NetworkService")

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10)

try:
    driver.get("https://practicetestautomation.com/practice-test-login/")
    time.sleep(5)  # Wait for 5 secs after you open the page
    driver.maximize_window()

    time.sleep(3)  # Wait for 3 secs before every action

    username_field = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='username']")))
    username_field.send_keys("student")

    time.sleep(3)  # Wait for 3 secs before every action

    password_field = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='password']")))
    password_field.send_keys("incorrectPassword")

    time.sleep(3)  # Wait for 3 secs before every action

    submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='submit']")))
    submit_button.click()

    time.sleep(3)  # Wait for 3 secs before every action

    error_message = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[text()='Your password is invalid!']")))

    if error_message.is_displayed():
        print("Test Passed: Error message is displayed.")
        sys.exit(0)
    else:
        print("Test Failed: Error message is not displayed.")
        sys.exit(1)

except Exception as e:
    print(f"Test Failed: {str(e)}")
    sys.exit(1)
finally:
    driver.quit()
