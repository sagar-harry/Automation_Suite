
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import sys

def wait_for_element(driver, by, value, timeout=10):
    end_time = time.time() + timeout
    while time.time() < end_time:
        try:
            element = driver.find_element(by, value)
            if element.is_displayed():
                return element
        except:
            pass
    raise Exception(f"Element {value} not found after {timeout} seconds")

def main():
    try:
        # Set up Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-features=NetworkService")
        
        # Initialize Chrome driver
        driver = webdriver.Chrome(options=chrome_options)

        # Open the website
        driver.get("https://saucedemo.com/")
        driver.maximize_window()
        time.sleep(5)

        # Log in
        wait_for_element(driver, By.XPATH, '//*[@id="user"]').send_keys("standard")
        time.sleep(3)
        wait_for_element(driver, By.XPATH, '//*[@id="password"]').send_keys("secret_sauce")
        time.sleep(3)
        wait_for_element(driver, By.XPATH, '//*[@id="login-button"]').click()
        time.sleep(3)

        # Add items to cart
        wait_for_element(driver, By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
        time.sleep(3)
        wait_for_element(driver, By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
        time.sleep(3)

        # Proceed to checkout
        wait_for_element(driver, By.XPATH, '//*[@id="123"]/a').click()
        time.sleep(3)
        wait_for_element(driver, By.XPATH, '//*[@id="checkout"]').click()
        time.sleep(3)

        # Enter checkout information
        wait_for_element(driver, By.XPATH, '//*[@id="first-name"]').send_keys("Jonnathan")
        time.sleep(3)
        wait_for_element(driver, By.XPATH, '//*[@id="last-name"]').send_keys("K")
        time.sleep(3)
        wait_for_element(driver, By.XPATH, '//*[@id="postal-code"]').send_keys("10007")
        time.sleep(3)
        wait_for_element(driver, By.XPATH, '//*[@id="continue"]').click()
        time.sleep(3)

        # Finish purchase
        wait_for_element(driver, By.XPATH, '//*[@id="finish"]').click()
        time.sleep(3)
        wait_for_element(driver, By.XPATH, '//*[@id="back-to-products"]').click()
        time.sleep(3)

        # Log out
        wait_for_element(driver, By.XPATH, '//*[@id="react-burger-menu-btn"]').click()
        time.sleep(3)
        wait_for_element(driver, By.XPATH, '//*[@id="logout_sidebar_link"]').click()
        time.sleep(3)

        # Capture screenshot before closing
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        driver.save_screenshot(f"C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\screenshot_{timestamp}.png")

        # Close driver
        driver.quit()
        
        sys.exit(0)
    except Exception as e:
        # Capture screenshot on error
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        driver.save_screenshot(f"C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\error_screenshot_{timestamp}.png")
        driver.quit()
        # Log the exception before exiting
        print(f"Test failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
