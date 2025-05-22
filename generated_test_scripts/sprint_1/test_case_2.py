
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import sys

try:
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-features=NetworkService")

    # Initialize WebDriver
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    # Go to the URL
    driver.get("https://saucedemo.com/")
    time.sleep(5)

    # Login
    driver.find_element(By.XPATH, "//*[@id='user-name']").send_keys("standard_user")
    time.sleep(3)
    driver.find_element(By.XPATH, "//*[@id='password']").send_keys("secret_sauce")
    time.sleep(3)
    driver.find_element(By.XPATH, "//*[@id='login-button']").click()
    time.sleep(3)

    # Add 'Bike Light' to Cart
    driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-bike-light']").click()
    time.sleep(3)

    # Add 'Fleece Jacket' to Cart
    driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-bolt-t-shirt']").click()
    time.sleep(3)

    # Proceed to Checkout
    driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']/a").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//*[@id='checkout']").click()
    time.sleep(3)

    # Enter Checkout Details
    driver.find_element(By.XPATH, "//*[@id='first-name']").send_keys("Jonnathan")
    time.sleep(3)
    driver.find_element(By.XPATH, "//*[@id='last-name']").send_keys("K")
    time.sleep(3)
    driver.find_element(By.XPATH, "//*[@id='postal-code']").send_keys("10007")
    time.sleep(3)
    driver.find_element(By.XPATH, "//*[@id='continue']").click()
    time.sleep(3)

    # Verify Payment Information
    payment_info = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[1]")
    assert payment_info.is_displayed(), "Payment Information is not displayed"
    
    # Save Snapshot
    driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png")

    sys.exit(0)

except Exception as e:
    print(f"Test case failed: {e}")
    sys.exit(1)

finally:
    driver.quit()
