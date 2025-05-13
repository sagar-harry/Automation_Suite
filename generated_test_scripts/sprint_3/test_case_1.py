
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

# Initialize the Chrome options
chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--disable-features=NetworkService")

try:
    # Create a new instance of the Chrome driver
    driver = webdriver.Chrome(options=chrome_options)

    # Maximize the browser window
    driver.maximize_window()

    # Navigate to the target URL
    driver.get("https://example.com/login")
    time.sleep(5)

    # Wait for the username field to appear
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/form/p[1]"))
    )
    time.sleep(3)
    username_field.send_keys("testqa999@gmail.com")

    # Wait for the password field to appear
    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/form/p[2]"))
    )
    time.sleep(3)
    password_field.send_keys("abcd123")

    # Wait for the submit button to appear
    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='submit']"))
    )
    time.sleep(3)
    submit_button.click()

    # Define the successful login condition with a dummy success message
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'success-message'))
    )

    # If successful, save the snapshot
    driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\login_success.png")
    sys.exit(0)

except Exception as e:
    # If there is an error, save the snapshot
    driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\login_error.png")
    sys.exit(1)

finally:
    # Close the browser
    driver.quit()
