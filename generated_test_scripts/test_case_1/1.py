
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from compare_sentences import compare_sentences

def test_login():
    # Initialize Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")

    # Initialize the WebDriver
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Maximize window
        driver.maximize_window()

        # Open the SauceDemo login page
        driver.get("https://www.saucedemo.com")

        # Wait for the username input to appear and Enter username
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='user-name']")))
        time.sleep(3)
        username_input = driver.find_element(By.XPATH, "//input[@id='user-name']")
        username_input.send_keys("standard_user")

        # Wait for the password input to appear and Enter password
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='password']")))
        time.sleep(3)
        password_input = driver.find_element(By.XPATH, "//input[@id='password']")
        password_input.send_keys("secret_sauce")

        # Wait for the login button to appear and Click the "Login" button
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='login-button']")))
        time.sleep(3)
        login_button = driver.find_element(By.XPATH, "//input[@id='login-button']")
        login_button.click()

        # Wait for the product listing title to appear
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[@class='title' and text()='Products']")))
        time.sleep(3)
        product_listing_title = driver.find_element(By.XPATH, "//span[@class='title' and text()='Products']")

        # Compare the text of the product listing title with the expected text
        if compare_sentences(product_listing_title.text, "Products"):
            sys.exit(0)  # Successful test case
        else:
            sys.exit(1)  # Failed test case

    except Exception as e:
        print(f"Test encountered an exception: {e}")
        sys.exit(1)  # Failed test case
    finally:
        driver.quit()

if __name__ == "__main__":
    test_login()
