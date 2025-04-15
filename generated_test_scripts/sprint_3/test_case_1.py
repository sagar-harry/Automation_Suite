
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def main():
    try:
        # Set up Selenium with Chrome options
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--disable-features=NetworkService")
        
        # Initialize the webdriver
        driver = webdriver.Chrome(options=chrome_options)

        # Open the web page
        driver.get("https://saucedemo.com/")
        time.sleep(5)
        driver.maximize_window()
        
        # Wait function
        def wait_for_element(by, value):
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((by, value)))
        
        # Log in to the site
        wait_for_element(By.XPATH, '//*[@id="user"]')
        username = driver.find_element(By.XPATH, '//*[@id="user"]')
        password = driver.find_element(By.XPATH, '//*[@id="password"]')
        login_button = driver.find_element(By.XPATH, '//*[@id="login-button"]')

        username.send_keys("standard")
        time.sleep(3)
        password.send_keys("secret_sauce")
        time.sleep(3)
        login_button.click()

        # Add items to the cart
        wait_for_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')
        bike_light = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')
        time.sleep(3)
        bike_light.click()

        wait_for_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
        fleece_jacket = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
        time.sleep(3)
        fleece_jacket.click()
        
        # Proceed to cart and checkout
        wait_for_element(By.XPATH, '//*[@id="123"]/a')
        cart_icon = driver.find_element(By.XPATH, '//*[@id="123"]/a')
        time.sleep(3)
        cart_icon.click()

        wait_for_element(By.XPATH, '//*[@id="checkout"]')
        checkout_button = driver.find_element(By.XPATH, '//*[@id="checkout"]')
        time.sleep(3)
        checkout_button.click()

        # Fill user info
        wait_for_element(By.XPATH, '//*[@id="first-name"]')
        first_name = driver.find_element(By.XPATH, '//*[@id="first-name"]')
        last_name = driver.find_element(By.XPATH, '//*[@id="last-name"]')
        postal_code = driver.find_element(By.XPATH, '//*[@id="postal-code"]')

        first_name.send_keys("Jonnathan")
        time.sleep(3)
        last_name.send_keys("K")
        time.sleep(3)
        postal_code.send_keys("10007")
        time.sleep(3)
        
        # Complete purchase
        wait_for_element(By.XPATH, '//*[@id="continue"]')
        continue_button = driver.find_element(By.XPATH, '//*[@id="continue"]')
        time.sleep(3)
        continue_button.click()
        
        wait_for_element(By.XPATH, '//*[@id="finish"]')
        finish_button = driver.find_element(By.XPATH, '//*[@id="finish"]')
        time.sleep(3)
        finish_button.click()

        # logout process
        wait_for_element(By.XPATH, '//*[@id="react-burger-menu-btn"]')
        logout_sidebar = driver.find_element(By.XPATH, '//*[@id="react-burger-menu-btn"]')
        time.sleep(3)
        logout_sidebar.click()

        wait_for_element(By.XPATH, '//*[@id="logout_sidebar_link"]')
        logout_button = driver.find_element(By.XPATH, '//*[@id="logout_sidebar_link"]')
        time.sleep(3)
        logout_button.click()

        # Capture page screenshot
        driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\screenshot.png")

        # Clean up and log results
        driver.quit()
        sys.exit(0)

    except Exception as e:
        driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\error_screenshot.png")
        print(f"An exception occurred: {str(e)}")
        if 'driver' in locals():
            driver.quit()
        sys.exit(1)

if __name__ == "__main__":
    main()
