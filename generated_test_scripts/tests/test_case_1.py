
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

try:
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-features=NetworkService")

    # Initialize driver
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()

    # Open the page
    driver.get("https://practicetestautomation.com/practice-test-login/")
    time.sleep(5)  # Wait for 5 seconds after opening the page

    # Wait for the username field
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='username']"))
    )

    # Enter the username
    username_field = driver.find_element(By.XPATH, "//input[@name='username']")
    time.sleep(3)  # Wait for 3 seconds
    username_field.send_keys('student')

    # Wait for the password field
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='password']"))
    )

    # Enter the password
    password_field = driver.find_element(By.XPATH, "//input[@name='password']")
    time.sleep(3)  # Wait for 3 seconds
    password_field.send_keys('Password123')

    # Wait for submit button
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='submit']"))
    )

    # Click the submit button
    submit_button = driver.find_element(By.XPATH, "//*[@id='submit']")
    time.sleep(3)  # Wait for 3 seconds
    submit_button.click()

    # Verify the success message
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='loop-container']/div/article/div[1]/h1"))
    )
    success_message = driver.find_element(By.XPATH, "//*[@id='loop-container']/div/article/div[1]/h1")

    if "Logged In Successfully" in success_message.text:
        driver.quit()
        sys.exit(0)
    else:
        driver.quit()
        sys.exit(1)

except Exception as e:
    print(f"Test failed: {e}")
    driver.quit()
    sys.exit(1)
