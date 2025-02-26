
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login(driver):
    username_locator = '//*[@id="user-name"]'
    password_locator = '//*[@id="password"]'
    login_button_locator = '//*[@id="login-button"]'

    driver.get("https://saucedemo.com/")
    time.sleep(5)
    driver.find_element(By.XPATH, username_locator).send_keys("standard_user")
    driver.find_element(By.XPATH, password_locator).send_keys("secret_sauce")
    driver.find_element(By.XPATH, login_button_locator).click()

def main():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--disable-features=NetworkService")

    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()

    try:
        login(driver)
        time.sleep(3)

        bike_light_locator = '//*[@id="add-to-cart-sauce-labs-bike-light"]'
        fleece_jacket_locator = '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]'
        cart_count_locator = '//*[@id="shopping_cart_container"]/a/span'
        remove_bike_light_locator = '//*[@id="remove-sauce-labs-bike-light"]'
        remove_fleece_jacket_locator = '//*[@id="remove-sauce-labs-fleece-jacket"]'
        add_bolt_tshirt_locator = '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, bike_light_locator))).click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, fleece_jacket_locator))).click()
        time.sleep(3)

        cart_badge = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, cart_count_locator)))
        assert cart_badge.text == '2', "Cart badge count is not 2"

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, remove_bike_light_locator))).click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, remove_fleece_jacket_locator))).click()
        time.sleep(3)

        cart_elements = driver.find_elements(By.XPATH, cart_count_locator)
        assert len(cart_elements) == 0, "Cart count element should not exist"

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, add_bolt_tshirt_locator))).click()
        time.sleep(3)

        cart_badge = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, cart_count_locator)))
        assert cart_badge.text == '1', "Cart badge count is not 1"

        driver.get_screenshot_as_file("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\final_state.png")
        sys.exit(0)
        
    except Exception as e:
        driver.get_screenshot_as_file("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\error_state.png")
        sys.exit(1)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
