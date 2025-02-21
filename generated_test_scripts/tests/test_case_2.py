
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

def test_login_error_message():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-notifications")
    options.add_argument("--incognito")
    options.add_argument("--disable-features=NetworkService")

    driver = webdriver.Chrome(options=options)
    driver.get("https://practicetestautomation.com/practice-test-login/")

    time.sleep(5)
    driver.maximize_window()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='username']"))
    )
    
    time.sleep(3)
    username_field = driver.find_element(By.XPATH, "//input[@name='username']")
    username_field.send_keys("incorrectUser")

    time.sleep(3)
    password_field = driver.find_element(By.XPATH, "//input[@name='password']")
    password_field.send_keys("Password123")

    time.sleep(3)
    submit_button = driver.find_element(By.XPATH, "//*[@id='submit']")
    submit_button.click()

    time.sleep(3)
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='error']"))
        )
        error_message = driver.find_element(By.XPATH, "//*[@id='error']").text
        if error_message.lower() == "your username is invalid!":
            exit_code = 0
        else:
            exit_code = 1
    except:
        exit_code = 1

    driver.quit()
    sys.exit(exit_code)

if __name__ == "__main__":
    test_login_error_message()
