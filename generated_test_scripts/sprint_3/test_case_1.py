
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login():
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-features=NetworkService")

    driver = webdriver.Chrome(options=options)

    try:
        driver.maximize_window()
        driver.get("http://your-url-here.com")

        time.sleep(5)  # Wait after opening the page

        # Wait for username field
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/form/p[1]"))
        )
        username_field = driver.find_element(By.XPATH, "/html/body/div[3]/form/p[1]")

        time.sleep(3)  # Wait before performing the action
        username_field.send_keys("testqa999@gmail.com")

        # Wait for password field
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/form/p[2]"))
        )
        password_field = driver.find_element(By.XPATH, "/html/body/div[3]/form/p[2]")

        time.sleep(3)  # Wait before performing the action
        password_field.send_keys("abcd123")

        # Wait for submit button
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='submit']"))
        )
        submit_button = driver.find_element(By.XPATH, "//*[@id='submit']")

        time.sleep(3)  # Wait before performing the action
        submit_button.click()

        # Validation logic should be placed here

        # If tests passed
        time.sleep(3)
        driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\success_screenshot.png")
        sys.exit(0)

    except Exception as e:
        driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\error_screenshot.png")
        sys.exit(1)
    
    finally:
        driver.quit()

# Run the test
test_login()
