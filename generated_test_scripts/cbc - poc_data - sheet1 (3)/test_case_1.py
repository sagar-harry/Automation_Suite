
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

def test_ui_login():
    options = Options()
    options.headless = True
    options.add_argument("--disable-notifications")
    options.add_argument("--incognito")
    options.add_argument("--disable-features=NetworkService")

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    try:
        driver.get('https://practicetestautomation.com/practice-test-login/')
        time.sleep(5)

        wait = WebDriverWait(driver, 10)

        # Wait for and enter username
        wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='username']"))).send_keys("student")
        time.sleep(3)

        # Wait for and enter password
        wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='password']"))).send_keys("Password123")
        time.sleep(3)

        # Wait for and click submit button
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='submit']"))).click()
        time.sleep(3)

        # Wait for and verify success message
        message_box = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='loop-container']/div/article/div[1]/h1")))
        assert message_box.text == "Logged In Successfully"

        driver.quit()
        sys.exit(0)

    except Exception as e:
        driver.quit()
        sys.exit(1)

if __name__ == "__main__":
    test_ui_login()
