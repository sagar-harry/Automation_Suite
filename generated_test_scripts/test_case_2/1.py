
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from compare_sentences import compare_sentences

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--start-maximized")

# Initialize WebDriver
driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 10)

try:
    # Step 1: Given the browser is at the SauceDemo login page
    driver.get("https://www.saucedemo.com")
    time.sleep(3)

    # Step 2: When the user enters username `standard_user` and password `secret_sauce`
    username_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='user-name']")))
    password_input = driver.find_element(By.XPATH, "//input[@id='password']")
    username_input.send_keys("standard_user")
    time.sleep(3)
    password_input.send_keys("secret_sauce")
    time.sleep(3)

    # Step 3: And clicks on the login button
    login_button = driver.find_element(By.XPATH, "//input[@id='login-button']")
    login_button.click()
    time.sleep(3)

    # Step 4: Then the user should be redirected to the product listing page
    wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='title' and text()='Products']")))

    # Step 5: When the user clicks on the `Add to cart` button for the `Sauce Labs Backpack`
    add_to_cart_button = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
    add_to_cart_button.click()
    time.sleep(3)

    # Step 6: And navigates to the shopping cart by clicking the cart icon
    cart_icon = driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
    cart_icon.click()
    time.sleep(3)

    # Step 7: Then the Shopping Cart page should be displayed with the `Sauce Labs Backpack` listed
    cart_item_name = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='inventory_item_name' and text()='Sauce Labs Backpack']")))
    
    # Use compare_sentences to verify item name matches exactly
    assert compare_sentences(cart_item_name.text, "Sauce Labs Backpack")

    # Exit indicating pass
    sys.exit(0)

except Exception as e:
    print(f"Test failed due to: {e}")
    # Exit indicating failure
    sys.exit(1)

finally:
    driver.quit()

