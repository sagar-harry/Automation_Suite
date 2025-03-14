
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

try:
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--incognito")
    options.add_argument('--disable-notifications')
    options.add_argument('--disable-popup-blocking')
    options.add_argument('--disable-features=NetworkService')

    driver = webdriver.Chrome(options=options)

    driver.get("https://saucedemo.com/")
    time.sleep(5)  # Wait for 5 secs after opening the page

    # Login
    wait = WebDriverWait(driver, 10)
    username_input = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="user-name"]')))
    username_input.send_keys("standard_user")

    password_input = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]')))
    password_input.send_keys("secret_sauce")

    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="login-button"]')))
    login_button.click()
    time.sleep(3)

    # Add Bike Light
    bike_light = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')))
    bike_light.click()
    time.sleep(3)

    # Add Fleece Jacket
    fleece_jacket = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]')))
    fleece_jacket.click()
    time.sleep(3)

    # Verify cart count is '2'
    cart_count = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))
    assert cart_count.text == '2', "Cart count is not '2'"

    # Remove Bike Light
    remove_bike_light = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="remove-sauce-labs-bike-light"]')))
    remove_bike_light.click()
    time.sleep(3)

    # Remove Fleece Jacket
    remove_fleece_jacket = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="remove-sauce-labs-fleece-jacket"]')))
    remove_fleece_jacket.click()
    time.sleep(3)

    # Verify cart count element does not exist
    try:
        cart_count_disappeared = wait.until(EC.invisibility_of_element((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))
    except Exception as e:
        raise AssertionError("Cart count element still exists")

    # Add Bolt T-Shirt
    bolt_tshirt = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')))
    bolt_tshirt.click()
    time.sleep(3)

    # Verify cart badge displays '1'
    cart_count = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))
    assert cart_count.text == '1', "Cart count is not '1'"

    # Save the snapshot of the page
    driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png")

    driver.quit()
    sys.exit(0)

except Exception as e:
    driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\error_screenshot.png")
    print(e)
    driver.quit()
    sys.exit(1)
