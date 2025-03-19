
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up WebDriver options
chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-features=NetworkService")

# Initialize WebDriver
driver = webdriver.Chrome(options=chrome_options)

try:
    driver.get("https://saucedemo.com/")
    time.sleep(5)  # Wait for 5 seconds after page load
    driver.maximize_window()

    # Login
    username_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="user-name"]'))
    )
    username_field.send_keys("standard_user")
    time.sleep(3)

    password_field = driver.find_element(By.XPATH, '//*[@id="password"]')
    password_field.send_keys("secret_sauce")
    time.sleep(3)

    login_button = driver.find_element(By.XPATH, '//*[@id="login-button"]')
    login_button.click()
    time.sleep(3)

    # Add items to cart
    bike_light = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))
    )
    bike_light.click()
    time.sleep(3)

    fleece_jacket = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
    fleece_jacket.click()
    time.sleep(3)

    # Checkout process
    cart_icon = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
    cart_icon.click()
    time.sleep(3)

    checkout = driver.find_element(By.XPATH, '//*[@id="checkout"]')
    checkout.click()
    time.sleep(3)

    first_name = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="first-name"]'))
    )
    first_name.send_keys("Jonnathan")
    time.sleep(3)

    last_name = driver.find_element(By.XPATH, '//*[@id="last-name"]')
    last_name.send_keys("K")
    time.sleep(3)

    postal_code = driver.find_element(By.XPATH, '//*[@id="postal-code"]')
    postal_code.send_keys("10007")
    time.sleep(3)

    continue_button = driver.find_element(By.XPATH, '//*[@id="continue"]')
    continue_button.click()
    time.sleep(3)

    finish_button = driver.find_element(By.XPATH, '//*[@id="finish"]')
    finish_button.click()
    time.sleep(3)

    # Return to home and logout
    back_to_products = driver.find_element(By.XPATH, '//*[@id="back-to-products"]')
    back_to_products.click()
    time.sleep(3)

    logout_sidebar = driver.find_element(By.XPATH, '//*[@id="react-burger-menu-btn"]')
    logout_sidebar.click()
    time.sleep(3)

    logout_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="logout_sidebar_link"]'))
    )
    logout_button.click()
    time.sleep(3)

    # Capture screenshot
    driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png")

    sys.exit(0)

except Exception as e:
    print(f"Test case failed due to: {e}")
    driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\error_screenshot.png")
    sys.exit(1)

finally:
    driver.quit()
