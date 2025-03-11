
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import sys

def wait_for_element(driver, by, path):
    for _ in range(10):
        try:
            element = driver.find_element(by, path)
            return element
        except:
            time.sleep(0.5)
    raise Exception(f'Element not found: {path}')

def main():
    try:
        options = Options()
        options.add_argument("--disable-notifications")
        options.add_argument("--incognito")
        options.add_argument("--disable-features=NetworkService")

        driver = webdriver.Chrome(options=options)
        driver.get("https://saucedemo.com/")
        time.sleep(5)
        
        driver.maximize_window()
        time.sleep(3)
        
        # Login
        username = wait_for_element(driver, By.XPATH, '//*[@id="user-name"]')
        username.send_keys("standard_user")
        time.sleep(3)

        password = wait_for_element(driver, By.XPATH, '//*[@id="password"]')
        password.send_keys("secret_sauce")
        time.sleep(3)

        login_button = wait_for_element(driver, By.XPATH, '//*[@id="login-button"]')
        login_button.click()
        time.sleep(3)

        # Add Bike Light
        bike_light = wait_for_element(driver, By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')
        bike_light.click()
        time.sleep(3)

        # Add Fleece Jacket
        fleece_jacket = wait_for_element(driver, By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]')
        fleece_jacket.click()
        time.sleep(3)

        # Check Cart Badge
        cart_badge = wait_for_element(driver, By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
        assert cart_badge.text == '2', "Cart badge does not display '2'"
        time.sleep(3)

        # Remove Bike Light
        remove_bike_light = wait_for_element(driver, By.XPATH, '//*[@id="remove-sauce-labs-bike-light"]')
        remove_bike_light.click()
        time.sleep(3)

        # Remove Fleece Jacket
        remove_fleece_jacket = wait_for_element(driver, By.XPATH, '//*[@id="remove-sauce-labs-fleece-jacket"]')
        remove_fleece_jacket.click()
        time.sleep(3)

        # Check Cart Count Element Not Exist
        try:
            driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
            raise Exception("Cart count element still exists")
        except:
            pass
        time.sleep(3)

        # Add Bolt T-Shirt
        add_bolt_t_shirt = wait_for_element(driver, By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
        add_bolt_t_shirt.click()
        time.sleep(3)

        # Assert Cart Badge shows '1'
        cart_badge = wait_for_element(driver, By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
        assert cart_badge.text == '1', "Cart badge does not display '1'"
        
        driver.save_screenshot(r'C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\final_state.png')
        
        sys.exit(0)

    except Exception as e:
        driver.save_screenshot(r'C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\error_state.png')
        print(str(e))
        sys.exit(1)

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
