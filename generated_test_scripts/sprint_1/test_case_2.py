
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import sys

# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--disable-features=NetworkService")
chrome_options.add_argument("start-maximized")

# Start the WebDriver
driver = webdriver.Chrome(options=chrome_options)

try:
    # Open the website
    driver.get("https://saucedemo.com/")
    time.sleep(5)

    # Login to the application
    driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys("standard_user")
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("secret_sauce")
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
    time.sleep(3)

    # Add 'Bike Light' and 'Fleece Jacket' to the cart
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
    time.sleep(3)

    # Proceed to checkout
    driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="checkout"]').click()
    time.sleep(3)

    # Enter checkout details
    driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys("Jonnathan")
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys("K")
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys("10007")
    time.sleep(3)

    # Continue to payment information
    driver.find_element(By.XPATH, '//*[@id="continue"]').click()
    time.sleep(3)

    # Verify that payment information is visible
    payment_info = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[1]')
    if payment_info.is_displayed():
        print("Test Case Passed")
        sys.exit(0)
    else:
        print("Test Case Failed")
        sys.exit(1)

except Exception as e:
    print(f"Test Case Failed due to {str(e)}")
    sys.exit(1)

finally:
    # Capture screenshot
    driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\screenshot.png")
    # Close the browser
    driver.quit()
