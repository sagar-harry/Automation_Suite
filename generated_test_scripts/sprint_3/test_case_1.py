
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time
import sys

def save_screenshot(driver, filename):
    driver.save_screenshot(filename)

def wait_for_element(driver, by, value):
    for _ in range(5):  # Try five times to find the element
        try:
            element = driver.find_element(by, value)
            if element:
                return element
        except NoSuchElementException:
            time.sleep(1)  # Wait 1 second before next try

def main():
    try:
        options = Options()
        options.add_argument("--incognito")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-features=NetworkService")

        driver = webdriver.Chrome(options=options)

        driver.get('https://saucedemo.com/')
        time.sleep(5)
        driver.maximize_window()

        # Logging in
        time.sleep(3)
        wait_for_element(driver, By.XPATH, "//input[@id='user-name']").send_keys("standard")
        wait_for_element(driver, By.XPATH, "//input[@id='password']").send_keys("secret_sauce")
        wait_for_element(driver, By.XPATH, "//input[@id='login-button']").click()

        # Add 'Bike Light' and 'Fleece Jacket' to the cart
        time.sleep(3)
        wait_for_element(driver, By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']").click()
        wait_for_element(driver, By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']").click()

        # Go to cart and checkout
        time.sleep(3)
        wait_for_element(driver, By.XPATH, "//a[@class='shopping_cart_link']").click()
        wait_for_element(driver, By.XPATH, "//button[@id='checkout']").click()

        # Enter checkout information
        time.sleep(3)
        wait_for_element(driver, By.XPATH, "//input[@id='first-name']").send_keys("Jonnathan")
        wait_for_element(driver, By.XPATH, "//input[@id='last-name']").send_keys("K")
        wait_for_element(driver, By.XPATH, "//input[@id='postal-code']").send_keys("10007")
        wait_for_element(driver, By.XPATH, "//input[@id='continue']").click()

        # Finish the purchase
        time.sleep(3)
        wait_for_element(driver, By.XPATH, "//button[@id='finish']").click()

        # Return to homepage and logout
        time.sleep(3)
        wait_for_element(driver, By.XPATH, "//button[@id='back-to-products']").click()

        # Open sidebar menu and logout
        wait_for_element(driver, By.XPATH, "//button[@id='react-burger-menu-btn']").click()
        time.sleep(3)
        wait_for_element(driver, By.XPATH, "//a[@id='logout_sidebar_link']").click()

        save_screenshot(driver, r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\final_screenshot.png")
        driver.quit()
        sys.exit(0)

    except Exception as e:
        save_screenshot(driver, r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\error_screenshot.png")
        driver.quit()
        sys.exit(1)

if __name__ == "__main__":
    main()
