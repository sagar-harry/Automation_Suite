
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys

def test_ui_scenario():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-features=NetworkService")

    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()

    try:
        # Open website
        driver.get("https://saucedemo.com/")
        time.sleep(5)
        
        # Login
        username_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='user-name']"))
        )
        password_input = driver.find_element(By.XPATH, "//*[@id='password']")
        login_button = driver.find_element(By.XPATH, "//*[@id='login-button']")

        username_input.send_keys('standard_user')
        time.sleep(3)
        password_input.send_keys('secret_sauce')
        time.sleep(3)
        login_button.click()
        time.sleep(3)

        # Add 'Bike Light' and 'Fleece Jacket' to the cart
        bike_light = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='add-to-cart-sauce-labs-bike-light']"))
        )
        fleece_jacket = driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-fleece-jacket']")
        
        bike_light.click()
        time.sleep(3)
        fleece_jacket.click()
        time.sleep(3)

        # Check if cart badge displays '2'
        cart_badge = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='shopping_cart_container']/a/span"))
        )
        assert cart_badge.text == '2', f"Expected cart badge to be '2' but got {cart_badge.text}"

        # Remove bike light and fleece jacket
        remove_bike_light = driver.find_element(By.XPATH, "//*[@id='remove-sauce-labs-bike-light']")
        remove_fleece_jacket = driver.find_element(By.XPATH, "//*[@id='remove-sauce-labs-fleece-jacket']")
        
        remove_bike_light.click()
        time.sleep(3)
        remove_fleece_jacket.click()
        time.sleep(3)

        # Check if cart count element doesn't exist
        try:
            cart_count_element = driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']/a/span")
        except:
            cart_count_element = None

        assert not cart_count_element, "Expected cart count element not to exist"

        # Add 'Bolt T-Shirt' to the cart
        add_bolt_tshirt = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='add-to-cart-sauce-labs-bolt-t-shirt']"))
        )
        add_bolt_tshirt.click()
        time.sleep(3)

        # Check if cart badge displays '1'
        cart_badge = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='shopping_cart_container']/a/span"))
        )
        assert cart_badge.text == '1', f"Expected cart badge to be '1' but got {cart_badge.text}"

        # Test case passed
        sys.exit(0)

    except Exception as e:
        print(f"Test case failed: {e}")
        driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\test_failure.png")
        # Test case failed
        sys.exit(1)
    
    finally:
        driver.quit()

test_ui_scenario()
