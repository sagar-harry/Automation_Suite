
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

# Initialize Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--disable-features=NetworkService")

# Initialize WebDriver
driver = webdriver.Chrome(options=chrome_options)

try:
    # Open the page and maximize
    driver.get('https://practicetestautomation.com/practice-test-login/')
    driver.maximize_window()
    time.sleep(5)

    # Wait for Username field and input data
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@name='username']")))
    time.sleep(3)
    username_field = driver.find_element(By.XPATH, "//input[@name='username']")
    username_field.send_keys('student')

    # Wait for Password field and input data
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@name='password']")))
    time.sleep(3)
    password_field = driver.find_element(By.XPATH, "//input[@name='password']")
    password_field.send_keys('incorrectPassword')

    # Wait for Submit button and click
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='submit']")))
    time.sleep(3)
    submit_button = driver.find_element(By.XPATH, "//*[@id='submit']")
    submit_button.click()

    # Verify error message
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[text()='Your password is invalid!']")))
    time.sleep(3)

    # Test passed
    sys.exit(0)

except Exception as e:
    # Test failed
    print(f"An error occurred: {e}")
    sys.exit(1)

finally:
    # Quit the driver
    driver.quit()
