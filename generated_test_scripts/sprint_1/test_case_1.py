
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import sys

# Configure Chrome Options
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-features=NetworkService")

try:
    # Initialize the WebDriver
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://saucedemo.com/")
    driver.implicitly_wait(10)
    time.sleep(5)
    driver.maximize_window()

    class LoginPage:
        def login(self, username, password):
            driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(username)
            driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
            driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
            time.sleep(3)

    # Perform Login
    login_page = LoginPage()
    login_page.login("standard_user", "secret_sauce")

    # Add bike light to cart
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
    time.sleep(3)

    # Add fleece jacket to cart
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]').click()
    time.sleep(3)

    # Verify cart badge displays '2'
    cart_badge = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
    assert cart_badge.text == '2', "Cart badge does not display '2'"

    # Remove bike light
    driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-bike-light"]').click()
    time.sleep(3)

    # Remove fleece jacket
    driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-fleece-jacket"]').click()
    time.sleep(3)

    # Verify cart count element doesn't exist
    cart_count_elements = driver.find_elements(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
    assert len(cart_count_elements) == 0, "Cart count element still exists"

    # Add Bolt T-Shirt to the cart
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
    time.sleep(3)

    # Verify cart badge displays '1'
    cart_badge = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
    assert cart_badge.text == '1', "Cart badge does not display '1'"

    # Save a screenshot
    driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\final_screenshot.png")

    # Exit the script with success code
    sys.exit(0)

except Exception as e:
    # Save a screenshot on failure
    driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\error_screenshot.png")
    print(f"Test Failed: {e}")
    sys.exit(1)

finally:
    # Quit the WebDriver
    driver.quit()
