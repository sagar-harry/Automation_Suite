
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import sys

def test_purchase_flow():
    try:
        # Chrome options to run in incognito mode, disable notifications, popups
        chrome_options = Options()
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--disable-features=NetworkService")

        # Initialize the Chrome driver
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()

        # Open the website
        driver.get("https://saucedemo.com/")
        time.sleep(5)

        # Login to the website
        def login(driver):
            driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard")
            time.sleep(3)
            driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")
            time.sleep(3)
            driver.find_element(By.XPATH, "//input[@id='login-button']").click()
            time.sleep(3)

        login(driver)

        # Add items to cart
        driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']").click()
        time.sleep(3)

        # Go to cart and proceed to checkout
        driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[@id='checkout']").click()
        time.sleep(3)

        # Enter checkout information
        driver.find_element(By.XPATH, "//input[@id='first-name']").send_keys("Jonnathan")
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@id='last-name']").send_keys("K")
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@id='postal-code']").send_keys("10007")
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@id='continue']").click()
        time.sleep(3)

        # Finish purchase
        driver.find_element(By.XPATH, "//button[@id='finish']").click()
        time.sleep(3)

        # Return to homepage
        driver.find_element(By.XPATH, "//button[@id='back-to-products']").click()
        time.sleep(3)

        # Logout
        driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//a[@id='logout_sidebar_link']").click()
        time.sleep(3)

        # Capture screenshot of final page
        driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\screenshot.png")

        # Close the driver
        driver.quit()

        # Exit with success code
        sys.exit(0)

    except Exception as e:
        # Capture screenshot of failure
        driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\screenshot_failure.png")

        # Close the driver
        driver.quit()

        # Print exception and exit with failure code
        print(e)
        sys.exit(1)

# Run the test
test_purchase_flow()
