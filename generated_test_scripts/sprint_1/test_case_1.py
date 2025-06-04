
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

try:
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--disable-features=NetworkService")

    # Initialize the webdriver
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get("https://saucedemo.com/")
    time.sleep(5)  # Wait for 5 seconds after opening the page

    # Log in
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='user-name']"))).send_keys("standard_user")
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='password']"))).send_keys("secret_sauce")
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='login-button']"))).click()
    time.sleep(3)

    # Add 'Bike Light' and 'Fleece Jacket' to the cart
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']"))).click()
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']"))).click()
    time.sleep(3)

    # Verify cart badge displays '2'
    cart_badge = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[@class='shopping_cart_badge']"))).text
    assert cart_badge == '2', f"Expected cart badge to be '2', but got '{cart_badge}'"

    # Remove 'Bike Light' and 'Fleece Jacket'
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='remove-sauce-labs-bike-light']"))).click()
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='remove-sauce-labs-fleece-jacket']"))).click()
    time.sleep(3)

    # Verify cart badge does not exist
    cart_badge_exists = driver.find_elements(By.XPATH, "//span[@class='shopping_cart_badge']")
    assert len(cart_badge_exists) == 0, "Cart badge should not exist"

    # Add 'Bolt T-Shirt' to the cart
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']"))).click()
    time.sleep(3)

    # Verify cart badge displays '1'
    cart_badge = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[@class='shopping_cart_badge']"))).text
    assert cart_badge == '1', f"Expected cart badge to be '1', but got '{cart_badge}'"

    # Take screenshot before closing
    driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\final_screen.png")

    # Close the webdriver
    driver.quit()

    # Exit with success code
    sys.exit(0)

except Exception as e:
    # Take screenshot on failure
    driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\error_screen.png")
    # Close the webdriver
    driver.quit()

    # Print the exception and exit with failure code
    print(e)
    sys.exit(1)
