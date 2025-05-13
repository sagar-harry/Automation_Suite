
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

try:
    # Set Chrome options
    chrome_options = Options()
    chrome_options.add_argument('--disable-notifications')
    chrome_options.add_argument('--disable-popup-blocking')
    chrome_options.add_argument('--incognito')
    chrome_options.add_argument('--disable-features=NetworkService')

    # Initialize WebDriver
    driver = webdriver.Chrome(options=chrome_options)

    # Maximize window
    driver.maximize_window()

    # Open URL
    driver.get("http://example.com/login")  # Replace with your login URL
    time.sleep(5)  # Wait for 5 seconds after opening the page

    # Locate username field and input
    username_locator = "/html/body/div[3]/form/p[1]"
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, username_locator)))
    time.sleep(3)  # Wait for 3 seconds before action
    username_field = driver.find_element(By.XPATH, username_locator)
    username_field.send_keys("testqa999@gmail.com")

    # Locate password field and input
    password_locator = "/html/body/div[3]/form/p[2]"
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, password_locator)))
    time.sleep(3)  # Wait for 3 seconds before action
    password_field = driver.find_element(By.XPATH, password_locator)
    password_field.send_keys("abcd123")

    # Locate and click submit button
    submit_button_locator = "//*[@id='submit']"
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, submit_button_locator)))
    time.sleep(3)  # Wait for 3 seconds before action
    submit_button = driver.find_element(By.XPATH, submit_button_locator)
    submit_button.click()

    # Optional: Add any verification here for successful login

    # Save a screenshot
    driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png")

    # Test passed
    sys.exit(0)

except Exception as e:
    # Print the error message if wanted, but don't output it as per instructions
    # print(str(e))
    driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\failure_screenshot.png")
    sys.exit(1)

finally:
    # Close the driver
    driver.quit()
