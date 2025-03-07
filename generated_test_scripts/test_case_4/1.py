
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from compare_sentences import compare_sentences

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--start-maximized")

# Initialize WebDriver
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://saucedemo.com/')

try:
    # Step 2: Find the username input field and enter the username
    username_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='user-name']"))
    )
    time.sleep(3)
    username_input.send_keys('standard_user')

    # Step 3: Find the password input field and enter the password
    password_input = driver.find_element(By.XPATH, "//input[@id='password']")
    time.sleep(3)
    password_input.send_keys('secret_sauce')

    # Step 4: Find the login button and click it
    login_button = driver.find_element(By.XPATH, "//input[@data-test='login-button']")
    time.sleep(3)
    login_button.click()

    # Step 5: Verify redirection to the Product Listing Page
    expected_url = 'https://saucedemo.com/inventory.html'
    WebDriverWait(driver, 10).until(EC.url_to_be(expected_url))
    actual_url = driver.current_url
    assert compare_sentences(expected_url, actual_url), "Redirection to Product Listing Page failed"

    # Step 6: Add a product to the cart
    add_to_cart_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-backpack']"))
    )
    time.sleep(3)
    add_to_cart_button.click()

    # Step 7: Go to the shopping cart page by clicking the cart icon
    cart_icon = driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
    time.sleep(3)
    cart_icon.click()

    # Step 8: Verify the presence of the cart item
    cart_item = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='cart_item']"))
    )
    assert cart_item is not None, "Cart item is not present"

    # Step 9: Remove product from cart
    remove_button = driver.find_element(By.XPATH, "//button[@data-test='remove-sauce-labs-backpack']")
    time.sleep(3)
    remove_button.click()

    # Step 10: Verify the product is removed
    cart_empty = not bool(driver.find_elements(By.XPATH, "//div[@class='cart_item']"))
    assert cart_empty, "Product is not removed from the cart"

    sys.exit(0)

except Exception as e:
    print(f"Test failed: {e}")
    sys.exit(1)

finally:
    driver.quit()
