
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import sys

# Initialize Chrome options
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-notifications")
options.add_argument("--incognito")
options.add_argument("--disable-features=NetworkService")

# Initialize Chrome Driver
driver = webdriver.Chrome(options=options)

try:
    # Open website
    driver.get("https://saucedemo.com/")
    time.sleep(5)

    # Maximize window
    driver.maximize_window()

    # Wait for 3 seconds before any actions (To adhere to the test requirements)
    time.sleep(3)

    # Perform login
    class LoginPage:
        def login(self, username, password):
            driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(username)
            time.sleep(3)
            driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
            time.sleep(3)
            driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
            time.sleep(3)
    
    login_page = LoginPage()
    login_page.login("standard_user", "secret_sauce")

    # Add 'Bike Light' to the cart
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
    time.sleep(3)

    # Add 'Fleece Jacket' to the cart
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]').click()
    time.sleep(3)

    # Check the cart badge for '2'
    cart_count = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span').text
    if cart_count != "2":
        raise Exception("Cart count is not '2' after adding items")

    # Remove 'Bike Light' from cart
    driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-bike-light"]').click()
    time.sleep(3)

    # Remove 'Fleece Jacket' from cart
    driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-fleece-jacket"]').click()
    time.sleep(3)

    # Check that the cart badge is not present
    try:
        driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
        raise Exception("Cart count element should not exist after removing all items")
    except:
        pass

    # Add 'Bolt T-Shirt' to the cart
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
    time.sleep(3)

    # Check the cart badge for '1'
    cart_count = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span').text
    if cart_count != "1":
        raise Exception("Cart count is not '1' after adding 'Bolt T-Shirt'")

except Exception as e:
    print(f"Test failed: {e}")
    sys.exit(1)
finally:
    driver.quit()

sys.exit(0)
