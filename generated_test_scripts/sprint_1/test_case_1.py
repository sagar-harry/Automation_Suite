
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

def main():
    try:
        # Chrome options
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-features=NetworkService")

        # Initialize webdriver
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        driver.get("https://saucedemo.com/")
        time.sleep(5)

        # Login
        driver.find_element(By.XPATH, "//*[@id='user-name']").send_keys("standard_user")
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id='password']").send_keys("secret_sauce")
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id='login-button']").click()
        time.sleep(3)

        # Add Bike Light to Cart
        bike_light = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='add-to-cart-sauce-labs-bike-light']"))
        )
        bike_light.click()
        time.sleep(3)

        # Add Fleece Jacket to Cart
        fleece_jacket = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='add-to-cart-sauce-labs-fleece-jacket']"))
        )
        fleece_jacket.click()
        time.sleep(3)

        # Verify Cart count is 2
        cart_badge = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='shopping_cart_container']/a/span"))
        )
        assert cart_badge.text == '2'

        # Remove Bike Light
        remove_bike_light = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='remove-sauce-labs-bike-light']"))
        )
        remove_bike_light.click()
        time.sleep(3)

        # Remove Fleece Jacket
        remove_fleece_jacket = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='remove-sauce-labs-fleece-jacket']"))
        )
        remove_fleece_jacket.click()
        time.sleep(3)

        # Verify Cart count element does not exist
        try:
            WebDriverWait(driver, 10).until_not(
                EC.presence_of_element_located((By.XPATH, "//*[@id='shopping_cart_container']/a/span"))
            )
        except TimeoutException:
            raise Exception("Cart count element still exists")

        # Add Bolt T-Shirt to Cart
        bolt_tshirt = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='add-to-cart-sauce-labs-bolt-t-shirt']"))
        )
        bolt_tshirt.click()
        time.sleep(3)

        # Verify Cart count is 1
        cart_badge = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='shopping_cart_container']/a/span"))
        )
        assert cart_badge.text == '1'

        # Test Passed
        driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png")
        sys.exit(0)
    
    except Exception as e:
        driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png")
        sys.exit(1)

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
