
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def test_checkout_payment_information():
    # Setup options for headless mode, incognito, and disable notifications
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-notifications")

    driver = webdriver.Chrome(options=chrome_options)
    try:
        # Open the website and maximize
        driver.get("https://saucedemo.com/")
        time.sleep(5)  # Wait for 5 seconds
        driver.maximize_window()

        # Log in
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys("standard_user")
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("secret_sauce")
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="login-button"]').click()

        # Add 'Bike Light' and 'Fleece Jacket' to the cart
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()

        # Go to cart
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()

        # Proceed to checkout
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="checkout"]').click()

        # Enter Checkout Information
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys("somename")
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys("lastname")
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys("123456")

        # Continue to Payment Information
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="continue"]').click()

        # Assert that Payment Information is visible
        time.sleep(3)
        payment_info_visible = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[1]').is_displayed()

        if payment_info_visible:
            print("Test case passed.")
            exit(0)
        else:
            print("Test case failed.")
            exit(1)

    except Exception as e:
        print("Test case failed due to exception:", e)
        exit(1)

    finally:
        driver.quit()

test_checkout_payment_information()
