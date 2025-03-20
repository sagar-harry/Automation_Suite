
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time

def test_cart_count():
    try:
        # Set up Chrome options
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--disable-features=NetworkService")

        # Initialize the webdriver
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()

        # Open the website
        driver.get("https://saucedemo.com/")
        time.sleep(5)

        # Wait until elements are visible
        wait = WebDriverWait(driver, 10)

        # Log in
        username_field = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="user-name"]')))
        password_field = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]')))
        login_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="login-button"]')))

        username_field.send_keys("standard_user")
        time.sleep(3)
        password_field.send_keys("secret_sauce")
        time.sleep(3)
        login_button.click()
        time.sleep(3)

        # Add Bike Light to the cart
        bike_light_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')))
        bike_light_button.click()
        time.sleep(3)

        # Add Fleece Jacket to the cart
        fleece_jacket_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')))
        fleece_jacket_button.click()
        time.sleep(3)

        # Verify cart count is '2'
        cart_count_element = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))
        cart_count = cart_count_element.text

        # Assert the cart count
        assert cart_count == "2", f"Expected cart count '2', but got '{cart_count}'"

        # Save screenshot upon success
        driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\test_success.png")
        
        sys.exit(0)

    except Exception as e:
        # Save screenshot on error
        driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\test_failure.png")
        print(f"Test failed: {str(e)}")
        sys.exit(1)

    finally:
        driver.quit()

if __name__ == "__main__":
    test_cart_count()
