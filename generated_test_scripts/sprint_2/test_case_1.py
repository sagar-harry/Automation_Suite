
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def perform_ui_test():
    try:
        # Set Chrome Options
        chrome_options = Options()
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument('--disable-features=NetworkService')
        
        # Initialize WebDriver
        driver = webdriver.Chrome(options=chrome_options)
        
        # Open the website and maximize the window
        driver.get("https://saucedemo.com/")
        time.sleep(5)  # Wait for 5 seconds
        driver.maximize_window()
        
        wait = WebDriverWait(driver, 10)
        
        # Login
        username = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="user-name"]')))
        password = driver.find_element(By.XPATH, '//*[@id="password"]')
        login_button = driver.find_element(By.XPATH, '//*[@id="login-button"]')
        
        time.sleep(3)  # Wait before action
        username.send_keys("standard_user")
        password.send_keys("secret_sauce")
        login_button.click()
        
        # Add 'Bike Light' to the cart
        time.sleep(3)  # Wait before action
        bike_light = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')))
        bike_light.click()
        
        # Add 'Fleece Jacket' to the cart
        time.sleep(3)  # Wait before action
        fleece_jacket = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
        fleece_jacket.click()
        
        # Click on the cart icon and proceed to checkout
        time.sleep(3)  # Wait before action
        cart_icon = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
        cart_icon.click()
        
        time.sleep(3)  # Wait before action
        checkout = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="checkout"]')))
        checkout.click()
        
        # Enter checkout information
        time.sleep(3)  # Wait before action
        first_name = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="first-name"]')))
        last_name = driver.find_element(By.XPATH, '//*[@id="last-name"]')
        postal_code = driver.find_element(By.XPATH, '//*[@id="postal-code"]')
        
        first_name.send_keys("Jonnathan")
        last_name.send_keys("K")
        postal_code.send_keys("10007")
        
        # Continue and complete the purchase
        time.sleep(3)  # Wait before action
        continue_button = driver.find_element(By.XPATH, '//*[@id="continue"]')
        continue_button.click()
        
        time.sleep(3)  # Wait before action
        finish_button = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="finish"]')))
        finish_button.click()
        
        # Click on the finish button and return to the homepage
        time.sleep(3)  # Wait before action
        back_to_products = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="back-to-products"]')))
        back_to_products.click()
        
        # Log out
        time.sleep(3)  # Wait before action
        logout_sidebar = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-burger-menu-btn"]')))
        logout_sidebar.click()
        
        time.sleep(3)  # Wait before action
        logout_button = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="logout_sidebar_link"]')))
        logout_button.click()
        
        # Save the snapshot of the page
        driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\final_screenshot.png")
        
        # Close the browser
        driver.quit()
        
        sys.exit(0)  # Test case passed
        
    except Exception as e:
        driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\error_screenshot.png")
        driver.quit()
        sys.exit(1)  # Test case failed

# Execute the test function
if __name__ == "__main__":
    perform_ui_test()
