
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-features=NetworkService")

    # Initialize WebDriver
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()

    # Go to the website
    driver.get("https://saucedemo.com/")
    time.sleep(5)  # Wait for the page to fully load

    # Page Elements
    username_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="user-name"]'))
    )
    password_input = driver.find_element(By.XPATH, '//*[@id="password"]')
    login_button = driver.find_element(By.XPATH, '//*[@id="login-button"]')

    # Login
    username_input.send_keys("standard_user")
    password_input.send_keys("secret_sauce")
    time.sleep(3)  # Pause before logging in
    login_button.click()

    # Add 'Bike Light' to the cart
    bike_light_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))
    )
    bike_light_button.click()
    time.sleep(3)  # Pause after clicking

    # Add 'Fleece Jacket' to the cart
    fleece_jacket_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]'))
    )
    fleece_jacket_button.click()
    time.sleep(3)  # Pause after clicking

    # Verify cart count is '2'
    cart_count = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span'))
    )
    assert cart_count.text == '2', "Cart count should be 2 after adding two items"

    # Remove 'Bike Light' from cart
    remove_bike_light_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="remove-sauce-labs-bike-light"]'))
    )
    remove_bike_light_button.click()
    time.sleep(3)  # Pause after clicking

    # Remove 'Fleece Jacket' from cart
    remove_fleece_jacket_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="remove-sauce-labs-fleece-jacket"]'))
    )
    remove_fleece_jacket_button.click()
    time.sleep(3)  # Pause after clicking

    # Verify cart count element shouldn't exist
    try:
        cart_count = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
        assert cart_count is None, "Cart count element should not exist"
    except:
        pass

    # Add 'Bolt T-Shirt' to the cart
    add_bolt_tshirt_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))
    )
    add_bolt_tshirt_button.click()
    time.sleep(3)  # Pause after clicking

    # Verify cart count is '1'
    cart_count = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span'))
    )
    assert cart_count.text == '1', "Cart count should be 1 after adding one item"

    # If all asserts passed, save screenshot and exit success
    driver.get_screenshot_as_file(
        'C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\page_snapshot.png'
    )
    sys.exit(0)

except Exception as e:
    print(e)
    driver.get_screenshot_as_file(
        'C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\error_snapshot.png'
    )
    sys.exit(1)

finally:
    driver.quit()
