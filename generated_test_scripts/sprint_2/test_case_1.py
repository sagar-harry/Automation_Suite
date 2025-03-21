
import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_purchase_flow():
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-features=NetworkService")

    try:
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get("https://saucedemo.com/")

        time.sleep(5)

        # Login
        username_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="user-name"]'))
        )
        username_field.send_keys("standard_user")
        time.sleep(3)

        password_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]'))
        )
        password_field.send_keys("secret_sauce")
        time.sleep(3)

        login_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="login-button"]'))
        )
        login_button.click()
        time.sleep(3)

        # Add items to the cart
        bike_light = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))
        )
        bike_light.click()
        time.sleep(3)

        fleece_jacket = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))
        )
        fleece_jacket.click()
        time.sleep(3)

        # Proceed to checkout
        cart_icon = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a'))
        )
        cart_icon.click()
        time.sleep(3)

        checkout_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="checkout"]'))
        )
        checkout_button.click()
        time.sleep(3)

        first_name_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="first-name"]'))
        )
        first_name_field.send_keys("Jonnathan")
        time.sleep(3)

        last_name_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="last-name"]'))
        )
        last_name_field.send_keys("K")
        time.sleep(3)

        postal_code_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="postal-code"]'))
        )
        postal_code_field.send_keys("10007")
        time.sleep(3)

        continue_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="continue"]'))
        )
        continue_button.click()
        time.sleep(3)

        finish_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="finish"]'))
        )
        finish_button.click()
        time.sleep(3)

        # Logout
        logout_sidebar = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="react-burger-menu-btn"]'))
        )
        logout_sidebar.click()
        time.sleep(3)

        logout_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="logout_sidebar_link"]'))
        )
        logout_button.click()
        time.sleep(3)

        # Screenshot
        driver.save_screenshot('C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\homepage.png')

        sys.exit(0)

    except Exception as e:
        driver.save_screenshot('C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\error.png')
        print(f"An error occurred: {e}")
        sys.exit(1)

    finally:
        driver.quit()

if __name__ == "__main__":
    test_purchase_flow()
