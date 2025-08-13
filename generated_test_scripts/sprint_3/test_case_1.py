
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import sys

try:
    # Set up options for Chrome
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--disable-features=NetworkService")
    
    # Initialize WebDriver
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(5)

    # Open the URL
    driver.get("https://saucedemo.com/")
    time.sleep(5)

    # Define LoginPage class
    class LoginPage:
        def login(self, username, password):
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys(username)
            time.sleep(3)
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(password)
            time.sleep(3)
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "login-button"))).click()
            time.sleep(3)

    # Log in
    login_page = LoginPage()
    login_page.login("standard", "secret_sauce")

    # Add 'Bike Light' to cart
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "add-to-cart-sauce-labs-bike-light"))).click()
    time.sleep(3)

    # Add 'Fleece Jacket' to cart
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "add-to-cart-sauce-labs-fleece-jacket"))).click()
    time.sleep(3)

    # Click on cart icon
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_link"))).click()
    time.sleep(3)

    # Proceed to checkout
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "checkout"))).click()
    time.sleep(3)

    # Enter checkout information
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "first-name"))).send_keys("Jonnathan")
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "last-name"))).send_keys("K")
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "postal-code"))).send_keys("10007")
    time.sleep(3)

    # Click 'Continue' and complete the purchase
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "continue"))).click()
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "finish"))).click()
    time.sleep(3)

    # Click 'Back Home' to return to homepage
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "back-to-products"))).click()
    time.sleep(3)

    # Log out
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "react-burger-menu-btn"))).click()
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "logout_sidebar_link"))).click()
    time.sleep(3)

    # Save snapshot of the page
    driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\screenshot.png")

    # Close browser
    driver.quit()
    sys.exit(0)

except Exception as e:
    print(f"An error occurred: {e}")
    driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\error_screenshot.png")
    driver.quit()
    sys.exit(1)
