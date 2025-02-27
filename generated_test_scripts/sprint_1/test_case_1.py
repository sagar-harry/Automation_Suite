
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import sys

try:
    # Configure Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--disable-features=NetworkService")

    # Initialize the WebDriver
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    
    # Open the website and wait
    driver.get("https://saucedemo.com/")
    time.sleep(5)
    
    # Log in using LoginPage class method
    driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys("standard_user")
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("secret_sauce")
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
    time.sleep(3)

    # Add 'Bike Light' to cart
    bike_light = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')
    bike_light.click()
    time.sleep(3)

    # Add 'Fleece Jacket' to cart
    fleece_jacket = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]')
    fleece_jacket.click()
    time.sleep(3)

    # Check cart badge for '2'
    cart_badge = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
    assert cart_badge.text == '2', f"Cart badge expected '2', but got {cart_badge.text}"

    # Remove 'Bike Light'
    remove_bike_light = driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-bike-light"]')
    remove_bike_light.click()
    time.sleep(3)

    # Remove 'Fleece Jacket'
    remove_fleece_jacket = driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-fleece-jacket"]')
    remove_fleece_jacket.click()
    time.sleep(3)

    # Check cart count element doesn't exist
    cart_elements_count = driver.find_elements(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
    assert len(cart_elements_count) == 0, "Cart count element should not exist, but it does."

    # Add 'Bolt T-Shirt' to cart
    bolt_tshirt = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
    bolt_tshirt.click()
    time.sleep(3)

    # Check cart badge for '1'
    cart_badge = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
    assert cart_badge.text == '1', f"Cart badge expected '1', but got {cart_badge.text}"

    # Test passed
    driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png")
    sys.exit(0)

except Exception as e:
    # Test failed
    driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\failed_screenshot.png")
    print(f"Test failed: {e}")
    sys.exit(1)

finally:
    # Close the driver
    driver.quit()
