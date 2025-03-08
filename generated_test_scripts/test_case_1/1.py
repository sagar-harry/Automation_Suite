
import sys
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from compare_sentences import compare_sentences

def test_login():
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    
    driver = webdriver.Chrome(options=options)

    try:
        # Maximize the browser window
        driver.maximize_window()
        
        # Navigate to the login page
        driver.get("https://www.saucedemo.com/")
        
        # Wait for the page to load
        sleep(3)

        # Locate username input and enter username
        username_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='user-name']"))
        )
        username_input.send_keys("standard_user")
        
        # Wait before next action
        sleep(3)

        # Locate password input and enter password
        password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='password']"))
        )
        password_input.send_keys("secret_sauce")
        
        # Wait before next action
        sleep(3)

        # Locate and click login button
        login_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='login-button']"))
        )
        login_button.click()
        
        # Wait before checking redirection
        sleep(3)

        # Validate redirection to the product listing page
        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://www.saucedemo.com/inventory.html")
        )
        
        # Wait before next action
        sleep(3)
        
        # Verify the page title
        product_page_title_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='title' and text()='Products']"))
        )
        
        # Using custom function to assert the page title
        expected_title = "Products"
        actual_title = product_page_title_element.text
        assert compare_sentences(actual_title, expected_title), "Page title does not match"
        
        # Exit with code 0 indicating the test passed
        sys.exit(0)

    except Exception as e:
        print(f"Test failed due to: {e}")
        # Exit with code 1 indicating the test failed
        sys.exit(1)
    
    finally:
        driver.quit()

if __name__ == "__main__":
    test_login()
