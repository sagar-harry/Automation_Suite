
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def login(driver):
    driver.get("https://saucedemo.com/")
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys("standard_user")
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("secret_sauce")
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
    time.sleep(3)

def test_case():
    try:
        options = Options()
        options.headless = True
        options.add_argument('--incognito')
        options.add_argument('--disable-notifications')
        
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()

        login(driver)
        
        # Adding bike light to cart
        bike_light = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))
        )
        bike_light.click()
        time.sleep(3)

        # Adding fleece jacket to cart
        fleece_jacket = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))
        )
        fleece_jacket.click()
        time.sleep(3)

        # Verifying cart count
        cart_count = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span'))
        )
        if cart_count.text != '2':
            driver.quit()
            exit(1)
        
        # Remove bike light from cart
        driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-bike-light"]').click()
        time.sleep(3)

        # Remove fleece jacket from cart
        driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-bolt-t-shirt"]').click()
        time.sleep(3)

        # Verify cart is empty
        time.sleep(3)
        cart_badge = driver.find_elements(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
        if len(cart_badge) != 0:
            driver.quit()
            exit(1)

        # Adding Bolt T-Shirt to cart
        bolt_tshirt = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))
        )
        bolt_tshirt.click()
        time.sleep(3)

        # Verifying cart count again
        cart_count_after_reset = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span'))
        )
        if cart_count_after_reset.text != '1':
            driver.quit()
            exit(1)

        # Test passed
        driver.quit()
        exit(0)
    
    except Exception as e:
        driver.quit()
        exit(1)

test_case()
