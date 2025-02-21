
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

def test_login():
    try:
        # Setup Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--disable-features=NetworkService")
        chrome_options.add_argument("--window-size=1920,1080")

        # Initialize WebDriver
        driver = webdriver.Chrome(options=chrome_options)

        # Open the page
        driver.get("https://practicetestautomation.com/practice-test-login/")
        time.sleep(5)

        # Maximize the page
        driver.maximize_window()

        # Locate username field and enter 'student'
        time.sleep(3)
        username_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@name='username']"))
        )
        username_field.send_keys("student")

        # Locate password field and enter 'Password123'
        time.sleep(3)
        password_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@name='password']"))
        )
        password_field.send_keys("Password123")

        # Locate and click the submit button
        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='submit']"))
        )
        submit_button.click()

        # Verify 'Logged In Successfully' message is visible
        time.sleep(3)
        message_box = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='loop-container']/div/article/div[1]/h1"))
        )
        assert message_box.text == "Logged In Successfully"

        # Exit with success code
        driver.quit()
        sys.exit(0)

    except Exception as e:
        print("Test failed:", e)
        driver.quit()
        sys.exit(1)

test_login()
