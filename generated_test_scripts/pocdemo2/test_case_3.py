
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys

def run_test():
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--disable-features=NetworkService")

    # Initialize the driver
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Open the page
        driver.get("https://practicetestautomation.com/practice-test-login/")
        driver.maximize_window()

        # Wait before actions
        time.sleep(5)

        # Enter the username
        username_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@name='username']"))
        )
        time.sleep(3)
        username_field.send_keys("student")

        # Enter the invalid password
        password_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@name='password']"))
        )
        time.sleep(3)
        password_field.send_keys("incorrectPassword")

        # Click submit
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='submit']"))
        )
        time.sleep(3)
        submit_button.click()

        # Verify error message
        error_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[text()='Your password is invalid!']"))
        )
        if error_message:
            driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png")
            sys.exit(0)

    except Exception as e:
        driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png")
        print(f"An error occurred: {e}")
        sys.exit(1)

    finally:
        driver.quit()

if __name__ == "__main__":
    run_test()
