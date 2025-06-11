
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import sys

def main():
    try:
        # Configure Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-popups")
        chrome_options.add_argument("--disable-features=NetworkService")
        
        # Initialize the WebDriver
        driver = webdriver.Chrome(options=chrome_options)
        
        # Open the webpage and maximize it
        driver.get('https://saucedemo.com/')
        time.sleep(5)
        driver.maximize_window()
        
        # Login
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard")
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@id='login-button']").click()
        
        # Add items to cart
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']").click()
        
        # Go to cart and checkout
        time.sleep(3)
        driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[@id='checkout']").click()
        
        # Enter checkout information
        time.sleep(3)
        driver.find_element(By.XPATH, '//input[@placeholder="First Name"]').send_keys("Jonathan")
        time.sleep(3)
        driver.find_element(By.XPATH, '//input[@placeholder="Last Name"]').send_keys("K")
        time.sleep(3)
        driver.find_element(By.XPATH, '//input[@placeholder="Zip/Postal Code"]').send_keys("10007")
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@id='continue']").click()
        
        # Finish the purchase
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[@id='finish']").click()
        
        # Return to homepage and logout
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[@id='back-to-products']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//a[@id='logout_sidebar_link']").click()
        
        # Screenshot to be taken before closing
        driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\screenshot.png")
        
        # Exit with success
        driver.quit()
        sys.exit(0)
        
    except Exception as e:
        # Screenshot to be taken before closing
        driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\screenshot.png")
        
        # Exit with failure
        driver.quit()
        sys.exit(1)

if __name__ == "__main__":
    main()
