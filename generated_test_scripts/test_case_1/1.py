
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from compare_sentences import compare_sentences

def test_login():
    # Chrome options for incognito and disabling notifications
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-notifications")

    # Initialize the Chrome driver
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Maximize the window
        driver.maximize_window()

        # Navigate to the login page
        driver.get("https://saucedemo.com")
        time.sleep(3)

        # Define locators
        username_locator = (By.XPATH, "//input[@id='user-name']")
        password_locator = (By.XPATH, "//input[@id='password']")
        login_button_locator = (By.XPATH, "//input[@id='login-button']")
        products_title_locator = (By.XPATH, "//span[@class='title' and text()='Products']")

        # Wait for username field to appear and enter username
        username_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located(username_locator))
        username_input.send_keys("standard_user")
        time.sleep(3)

        # Wait for password field to appear and enter password
        password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located(password_locator))
        password_input.send_keys("secret_sauce")
        time.sleep(3)

        # Click on the login button
        login_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(login_button_locator))
        login_button.click()
        time.sleep(3)

        # Verify redirection to the product listing page
        products_title = WebDriverWait(driver, 10).until(EC.presence_of_element_located(products_title_locator))
        assert compare_sentences(products_title.text, "Products"), "The title text is not as expected."

        print("Test case passed")
        sys.exit(0)

    except Exception as e:
        print(f"Test case failed: {e}")
        sys.exit(1)

    finally:
        # Quit the driver
        driver.quit()

if __name__ == "__main__":
    test_login()
