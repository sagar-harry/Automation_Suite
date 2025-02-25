
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import sys

def login(driver, username, password):
    driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(username)
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()

def main():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-notifications')
    options.add_argument('--incognito')
    options.add_argument('--disable-features=NetworkService')
    options.add_argument('--window-size=1920,1080')

    try:
        driver = webdriver.Chrome(options=options)
        driver.get("https://saucedemo.com/")
        time.sleep(5)
        driver.maximize_window()
        time.sleep(3)

        login(driver, "standard_user", "secret_sauce")
        
        time.sleep(3)        
        bike_light_button = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')
        fleece_jacket_button = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]')
        
        bike_light_button.click()
        time.sleep(3)
        fleece_jacket_button.click()
        time.sleep(3)
        
        cart_badge = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span').text
        if cart_badge != '2':
            sys.exit(1)
            
        remove_bike_light = driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-bike-light"]')
        remove_fleece_jacket = driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-fleece-jacket"]')
        
        remove_bike_light.click()
        time.sleep(3)
        remove_fleece_jacket.click()
        time.sleep(3)
        
        cart_badge = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span').text
        if cart_badge != '':
            sys.exit(1)
        
        add_bolt_tshirt = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
        
        add_bolt_tshirt.click()
        time.sleep(3)

        cart_badge = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span').text
        if cart_badge != '1':
            sys.exit(1)
        
        sys.exit(0)
    except Exception as e:
        print("Test failed:", e)
        sys.exit(1)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
