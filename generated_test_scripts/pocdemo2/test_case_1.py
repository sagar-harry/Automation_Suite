
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import sys

try:
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-features=NetworkService")

    driver = webdriver.Chrome(options=options)

    # Open the page
    driver.get('https://practicetestautomation.com/practice-test-login/')
    time.sleep(5)  # Wait for 5 seconds
    driver.maximize_window()

    # Wait until elements are found
    wait = WebDriverWait(driver, 10)

    # Enter the username
    time.sleep(3)
    username_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='username']")))
    username_field.send_keys('student')

    # Enter the password
    time.sleep(3)
    password_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='password']")))
    password_field.send_keys('Password123')

    # Click submit
    time.sleep(3)
    submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='submit']")))
    submit_button.click()

    # Verify successful login
    time.sleep(3)
    success_alert = wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'Logged In Successfully')]")))

    # Save snapshot of the page
    driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png")

    # Exit with code 0 if test passed
    sys.exit(0)

except Exception as e:
    # Save snapshot of the page
    driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png")

    # Print the exception and exit with code 1
    print(str(e))
    sys.exit(1)

finally:
    driver.quit()
