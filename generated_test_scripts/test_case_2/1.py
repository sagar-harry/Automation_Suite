
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from time import sleep
import sys
from compare_sentences import compare_sentences

# Set Chrome options to disable notifications, pop-ups, and enable incognito
options = Options()
options.add_argument("--disable-notifications")
options.add_argument("--disable-popup-blocking")
options.add_argument("--incognito")
options.add_argument("--start-maximized")

# Initialize the WebDriver
driver = webdriver.Chrome(options=options)
driver.maximize_window()

# Function to perform login
def login():
    driver.get('https://www.saucedemo.com/')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'user-name')))
    
    # Log in with credentials
    driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    driver.find_element(By.ID, 'login-button').send_keys(Keys.RETURN)
    sleep(3)  # Wait for 3 seconds

# Function to add product to the cart
def add_product_to_cart():
    try:
        # Wait for the add to cart button to be available and click it
        add_to_cart_button_xpath = "//button[@id='add-to-cart-sauce-labs-backpack']"
        add_to_cart_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, add_to_cart_button_xpath)))
        add_to_cart_button.click()
        sleep(3)  # Wait for 3 seconds

        # Verify cart badge
        cart_badge_xpath = "//div[@id='shopping_cart_container']//span[@class='shopping_cart_badge']"
        cart_badge = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, cart_badge_xpath)))
        badge_text = cart_badge.text

        assert compare_sentences(badge_text, "1"), "Cart badge does not display '1'."
        
        # Test successful
        sys.exit(0)
    except TimeoutException:
        print("Element not found. Test failed.")
        sys.exit(1)
    except AssertionError as ae:
        print(f"Assertion error: {str(ae)}")
        sys.exit(1)

# Execute the test case
try:
    login()
    add_product_to_cart()
finally:
    driver.quit()
