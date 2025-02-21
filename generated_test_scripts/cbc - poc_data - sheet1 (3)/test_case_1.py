
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Set up Chrome options for headless mode and incognito, disable notifications and NetworkService
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-features=NetworkService")

# Initialize the WebDriver
driver = webdriver.Chrome(options=chrome_options)

try:
    # Open the page
    driver.get("https://practicetestautomation.com/practice-test-login/")
    time.sleep(5)  # Wait for 5 seconds after opening the page

    # Maximize the page
    driver.maximize_window()
    time.sleep(3)  # Wait for 3 seconds before every action

    # Locate and fill the username field
    username_field = driver.find_element(By.XPATH, "//input[@name='username']")
    username_field.send_keys("student")
    time.sleep(3)  # Wait for 3 seconds before next action

    # Locate and fill the password field
    password_field = driver.find_element(By.XPATH, "//input[@name='password']")
    password_field.send_keys("Password123")
    time.sleep(3)  # Wait for 3 seconds before next action

    # Locate and click the submit button
    submit_button = driver.find_element(By.XPATH, "//*[@id='submit']")
    submit_button.click()
    time.sleep(3)  # Wait for 3 seconds for login action to complete

    # Verify the 'Logged In Successfully' message
    message_box = driver.find_element(By.XPATH, "//*[@id='loop-container']/div/article/div[1]/h1")
    assert "Logged In Successfully" in message_box.text
    exit_code = 0

except Exception:
    exit_code = 1

finally:
    # Close the WebDriver
    driver.quit()
    exit(exit_code)
