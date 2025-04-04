
import time
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def login(self, driver, username, password):
        driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(username)
        driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        driver.find_element(By.XPATH, '//*[@id="login-button"]').click()

def main():
    options = Options()
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--incognito")
    options.add_argument("--disable-features=NetworkService")

    # Initialize the Chrome driver
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    try:
        driver.get('https://saucedemo.com/')
        time.sleep(5)

        login_page = LoginPage()
        login_page.login(driver, 'standard_user', 'secret_sauce')
        time.sleep(3)

        # Add 'Bike Light' to cart
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))).click()
        time.sleep(3)
        
        # Add 'Fleece Jacket' to cart
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]'))).click()
        time.sleep(3)
        
        # Verify the cart badge displays '2'
        cart_badge = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))
        assert cart_badge.text == '2', "Cart badge does not display '2'"
        
        # Remove 'Bike Light'
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="remove-sauce-labs-bike-light"]'))).click()
        time.sleep(3)

        # Remove 'Fleece Jacket'
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="remove-sauce-labs-fleece-jacket"]'))).click()
        time.sleep(3)
        
        # Verify the cart count element doesn't exist
        cart_badge = driver.find_elements(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
        assert len(cart_badge) == 0, "Cart badge should not exist"
        
        # Add 'Bolt T-Shirt' to cart
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))).click()
        time.sleep(3)
        
        # Verify the cart badge displays '1'
        cart_badge = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))
        assert cart_badge.text == '1', "Cart badge does not display '1'"
        
        # Test case passed
        driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\screenshot.png")
        sys.exit(0)

    except Exception as e:
        print(f"Test case failed: {e}")
        driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\screenshot.png")
        sys.exit(1)

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
