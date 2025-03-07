
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from compare_sentences import compare_sentences
import time
import sys

# Setup chrome options
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--incognito")

# Initialize the driver
driver = webdriver.Chrome(options=chrome_options)

try:
    # Open the page
    driver.get("https://www.saucedemo.com")
    driver.maximize_window()
    
    # Wait for 3 seconds as per specifications
    time.sleep(3)

    # Pseudo code for login as it requires user to be authenticated
    # Implement login logic here.
    # Comment this out in case not required or if authentication logic is implemented elsewhere.
    # ...
    
    # Navigate to the shopping cart page
    shopping_cart_icon = driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link")
    shopping_cart_icon.click()
    
    # Wait for the cart page to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@data-test='cart-contents-container']"))
    )
    
    # Remove the "Sauce Labs Backpack"
    remove_button = driver.find_element(By.XPATH, "//button[@data-test='remove-sauce-labs-backpack']")
    remove_button.click()
    
    # Wait for the item to be removed
    time.sleep(3)  # Wait for the action to process
    
    # Verify "Sauce Labs Backpack" is removed
    cart_items = driver.find_elements(By.XPATH, "//div[@data-test='inventory-item-name']")
    item_removed = True
    for item in cart_items:
        if "Sauce Labs Backpack" in item.text:
            item_removed = False
            break
    
    # Assert the cart badge is empty
    cart_badge = driver.find_elements(By.XPATH, "//span[@data-test='shopping-cart-badge']")
    cart_badge_empty = not bool(cart_badge)
    
    # Use compare_sentences to assert the item removal
    item_removed_sentence = "The cart does not have Sauce Labs Backpack."
    item_expected_sentence = "The cart does not have Sauce Labs Backpack."
    
    if item_removed and cart_badge_empty and compare_sentences(item_removed_sentence, item_expected_sentence):
        sys.exit(0)  # Test case passed
    else:
        sys.exit(1)  # Test case failed

except Exception as e:
    print(f"An error occurred: {e}")
    sys.exit(1)
finally:
    driver.quit()
