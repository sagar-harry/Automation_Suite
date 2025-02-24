
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-features=NetworkService")

# Initialize WebDriver
driver = webdriver.Chrome(options=chrome_options)

try:
    # Open the page
    driver.get("https://practicetestautomation.com/practice-test-login/")
    time.sleep(5)  # Wait for 5 secs after opening the page

    # Maximize the page
    driver.maximize_window()

    # Wait for 3 secs before every action
    time.sleep(3)

    # Find the username field and enter username
    username_field = driver.find_element(By.XPATH, "//input[@name='username']")
    username_field.send_keys("student")

    # Wait for 3 secs
    time.sleep(3)

    # Find the password field and enter invalid password
    password_field = driver.find_element(By.XPATH, "//input[@name='password']")
    password_field.send_keys("incorrectPassword")

    # Wait for 3 secs
    time.sleep(3)

    # Find the submit button and click it
    submit_button = driver.find_element(By.XPATH, "//*[@id='submit']")
    submit_button.click()

    # Wait for 3 secs
    time.sleep(3)

    # Verify error message for "Your password is invalid!"
    try:
        error_message = driver.find_element(By.XPATH, "//div[text()='Your password is invalid!']")
        if error_message.is_displayed():
            print("Test Passed")
            exit(0)
        else:
            print("Test Failed")
            exit(1)
    except:
        print("Test Failed")
        exit(1)
finally:
    driver.quit()
