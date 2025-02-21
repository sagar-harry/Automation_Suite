
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

def run_test():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-features=NetworkService")

    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get("https://practicetestautomation.com/practice-test-login/")
        time.sleep(5)  # Wait for 5 seconds after opening the page
        driver.maximize_window()

        wait = WebDriverWait(driver, 10)

        # Enter the username
        username_field = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='username']")))
        time.sleep(3)  # Wait for 3 seconds before action
        username_field.send_keys("student")

        # Enter the password
        password_field = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='password']")))
        time.sleep(3)  # Wait for 3 seconds before action
        password_field.send_keys("Password123")

        # Click submit
        submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='submit']")))
        time.sleep(3)  # Wait for 3 seconds before action
        submit_button.click()

        # Verify 'Logged In Successfully' message is visible
        message_box = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='loop-container']/div/article/div[1]/h1")))
        time.sleep(3)  # Wait for 3 seconds before action
        assert "Logged In Successfully" in message_box.text

        sys.exit(0)

    except Exception as e:
        print(f"Test failed: {e}")
        sys.exit(1)

    finally:
        driver.quit()

if __name__ == "__main__":
    run_test()
