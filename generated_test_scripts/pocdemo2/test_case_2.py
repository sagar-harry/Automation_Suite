
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument('--incognito')
chrome_options.add_argument('--disable-notifications')
chrome_options.add_argument('--disable-popup-blocking')
chrome_options.add_argument('--disable-features=NetworkService')

# Launch Chrome
driver = webdriver.Chrome(options=chrome_options)

try:
    # Open the page
    driver.get("https://practicetestautomation.com/practice-test-login/")
    time.sleep(5)  # Wait for 5 seconds
    driver.maximize_window()

    # Wait for the Username field and enter username
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@name='username']"))
    )
    time.sleep(3)
    username_field = driver.find_element(By.XPATH, "//input[@name='username']")
    username_field.send_keys("incorrectUser")

    # Wait for the Password field and enter password
    time.sleep(3)
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@name='password']"))
    )
    password_field = driver.find_element(By.XPATH, "//input[@name='password']")
    password_field.send_keys("Password123")

    # Wait for the Submit button and click
    time.sleep(3)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='submit']"))
    )
    submit_button = driver.find_element(By.XPATH, "//*[@id='submit']")
    submit_button.click()

    # Verify error message
    time.sleep(3)
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[text()='Your username is invalid!']"))
    )
    
    # Save screenshot
    driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png")
    
    sys.exit(0)

except Exception as e:
    driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png")
    sys.exit(1)

finally:
    driver.quit()
