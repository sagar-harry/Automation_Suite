
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_ui_scenario():
    # Configure ChromeOptions
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-notifications')
    options.add_argument('--incognito')

    # Initialize the WebDriver
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://saucedemo.com/")
    time.sleep(5)

    try:
        # Login
        driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys("standard_user")
        driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("secret_sauce")
        driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
        time.sleep(3)
        
        # Add 'Bike Light' to cart
        bike_light = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))
        )
        bike_light.click()
        time.sleep(3)
        
        # Add 'Fleece Jacket' to cart
        fleece_jacket = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))
        )
        fleece_jacket.click()
        time.sleep(3)
        
        # Verify cart badge displays '2'
        cart_count = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span'))
        )
        assert cart_count.text == '2', f"Expected cart count to be '2' but found '{cart_count.text}'"
        
        # Reset cart by clicking on the cart and removing items
        driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
        time.sleep(3)
        
        # Assuming remove buttons are available within the cart page for added items, perform click actions
        remove_bike_light = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="remove-sauce-labs-bike-light"]'))
        )
        remove_bike_light.click()
        time.sleep(3)
        
        remove_fleece_jacket = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="remove-sauce-labs-bolt-t-shirt"]'))
        )
        remove_fleece_jacket.click()
        time.sleep(3)
        
        # Verify cart is empty
        cart_count = driver.find_elements(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
        assert len(cart_count) == 0, "Expected cart to be empty"
        
        # Add 'Bolt T-Shirt' to cart
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
        time.sleep(3)
        
        # Verify cart badge displays '1'
        cart_count = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span'))
        )
        assert cart_count.text == '1', f"Expected cart count to be '1' but found '{cart_count.text}'"

        driver.quit()
        exit(0)
        
    except Exception as e:
        print(str(e))
        driver.quit()
        exit(1)

if __name__ == "__main__":
    test_ui_scenario()
