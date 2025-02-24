
import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login(driver, username, password):
    driver.get('https://saucedemo.com/')
    time.sleep(5)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="user-name"]'))).send_keys(username)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]'))).send_keys(password)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="login-button"]'))).click()

def main():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--incognito")
    options.add_argument("--disable-features=NetworkService")
    
    driver = webdriver.Chrome(options=options)
    
    try:
        driver.maximize_window()
        login(driver, 'standard_user', 'secret_sauce')

        time.sleep(3)

        bike_light_elem = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')))
        bike_light_elem.click()
        time.sleep(3)

        fleece_jacket_elem = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')))
        fleece_jacket_elem.click()
        time.sleep(3)

        cart_count_elem = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))
        assert cart_count_elem.text == '2', "Cart badge should display '2'"
        
        # Assuming reset cart functionality, direct cart page is not mentioned
        # Reset the cart
        driver.get('https://saucedemo.com/cart.html') 
        time.sleep(3)

        remove_buttons = driver.find_elements(By.XPATH, '//button[contains(text(), "Remove")]')
        for btn in remove_buttons:
            btn.click()
            time.sleep(3)

        try:
            cart_count_elem = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
            assert False, "Cart should be empty"
        except:
            pass
        
        # Add 'Bolt T-Shirt'
        bolt_tshirt_elem = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')))
        bolt_tshirt_elem.click()
        time.sleep(3)

        cart_count_elem = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))
        assert cart_count_elem.text == '1', "Cart badge should display '1'"

        sys.exit(0)

    except Exception as e:
        print(f"Test case failed: {e}")
        sys.exit(1)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
