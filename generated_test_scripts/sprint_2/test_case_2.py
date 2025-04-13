
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import sys

options = Options()
options.add_argument("--disable-notifications")
options.add_argument("--incognito")
options.add_argument("--disable-features=NetworkService")
options.headless = True  # Running in headless mode

try:
    # Initialize the WebDriver
    driver = webdriver.Chrome(options=options)
    
    # Maximize the window
    driver.maximize_window()
    
    # Open the URL
    driver.get("https://saucedemo.com/")
    
    # Wait for 5+ seconds for the page to load
    time.sleep(5)
    
    # Log in using the LoginPage class method (assuming it's imported and properly set up)
    class LoginPage:
        @staticmethod
        def login(driver, username, password):
            driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(username)
            driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
            time.sleep(3)  # Wait before clicking the login button
            driver.find_element(By.XPATH, '//*[@id="login-button"]').click()

    LoginPage.login(driver, "standard_user", "secret_sauce")
    
    # Wait for the elements to appear
    time.sleep(3)
    
    # Add 'Bike Light' to the cart
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
    time.sleep(3)
    
    # Add 'Fleece Jacket' to the cart
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
    time.sleep(3)
    
    # Verify the cart badge displays '2'
    cart_badge = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
    assert cart_badge.text == '2', f"Expected cart badge to display '2', but got '{cart_badge.text}'"
    
    # Save a snapshot of the page
    driver.save_screenshot("C:/Users/Administrator/Desktop/QE_COE/automated_pipeline_2/captured_screenshots/cart_page.png")
    
    # Everything went fine
    sys.exit(0)

except Exception as e:
    # Save a snapshot of the page before exiting on error
    driver.save_screenshot("C:/Users/Administrator/Desktop/QE_COE/automated_pipeline_2/captured_screenshots/error_page.png")
    sys.print_exception(e)
    sys.exit(1)
finally:
    # Close the WebDriver
    driver.quit()
