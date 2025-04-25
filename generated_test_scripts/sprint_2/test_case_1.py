
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import sys

try:
    # Chrome options to disable notifications, pop-ups, and run in incognito mode
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--disable-features=NetworkService")

    # Initialize the WebDriver
    driver = webdriver.Chrome(options=chrome_options)

    # Go to the website
    driver.get("https://saucedemo.com/")
    time.sleep(5)  # Wait for 5 seconds

    # Maximize the window
    driver.maximize_window()

    # Wait for elements to load and perform actions
    def wait_and_find(by, value):
        return driver.find_element(by, value)

    # Log in
    wait_and_find(By.XPATH, '//*[@id="user-name"]').send_keys("standard_user")
    time.sleep(3)
    wait_and_find(By.XPATH, '//*[@id="password"]').send_keys("secret_sauce")
    time.sleep(3)
    wait_and_find(By.XPATH, '//*[@id="login-button"]').click()

    # Add items to the cart
    time.sleep(3)
    wait_and_find(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
    time.sleep(3)
    wait_and_find(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()

    # Go to cart
    time.sleep(3)
    wait_and_find(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()

    # Proceed to checkout
    time.sleep(3)
    wait_and_find(By.XPATH, '//*[@id="checkout"]').click()

    # Enter checkout information
    time.sleep(3)
    wait_and_find(By.XPATH, '//*[@id="first-name"]').send_keys("Jonnathan")
    time.sleep(3)
    wait_and_find(By.XPATH, '//*[@id="last-name"]').send_keys("K")
    time.sleep(3)
    wait_and_find(By.XPATH, '//*[@id="postal-code"]').send_keys("10007")

    # Continue and finish purchase
    time.sleep(3)
    wait_and_find(By.XPATH, '//*[@id="continue"]').click()
    time.sleep(3)
    wait_and_find(By.XPATH, '//*[@id="finish"]').click()

    # Return to homepage
    time.sleep(3)
    wait_and_find(By.XPATH, '//*[@id="back-to-products"]').click()

    # Logout
    time.sleep(3)
    wait_and_find(By.XPATH, '//*[@id="react-burger-menu-btn"]').click()
    time.sleep(3)
    wait_and_find(By.XPATH, '//*[@id="logout_sidebar_link"]').click()

    # Take a screenshot of the final page
    driver.save_screenshot(
        r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png"
    )

    # Exit successfully
    sys.exit(0)

except Exception as e:
    driver.save_screenshot(
        r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\error.png"
    )
    print(f"An exception occurred: {e}")
    sys.exit(1)

finally:
    # Close the driver
    driver.quit()
