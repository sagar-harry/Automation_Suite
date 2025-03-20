
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import sys

try:
    # Setup Chrome options
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-features=NetworkService")
    
    # Initialize WebDriver
    driver = webdriver.Chrome(options=chrome_options)

    # Open the website
    driver.get("https://saucedemo.com/")
    time.sleep(5)  # Wait for the page to load

    # Maximize the browser window
    driver.maximize_window()

    # Login Process
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys("standard_user")
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("secret_sauce")
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()

    # Add items to cart
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()

    # Go to cart
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()

    # Proceed to checkout
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="checkout"]').click()

    # Fill out checkout information
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys("Jonnathan")
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys("K")
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys("10007")
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="continue"]').click()

    # Complete the purchase
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="finish"]').click()

    # Return to homepage
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="back-to-products"]').click()

    # Logout process
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="react-burger-menu-btn"]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="logout_sidebar_link"]').click()

    # Capture screenshot
    driver.save_screenshot('C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\final_page.png')

    # Close the driver
    driver.quit()

    # Exit test case as passed
    sys.exit(0)

except Exception as e:
    driver.save_screenshot('C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\final_page.png')
    driver.quit()
    sys.exit(1)
