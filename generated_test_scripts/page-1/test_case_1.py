
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

# Initialize the Chrome driver
options = webdriver.ChromeOptions()
options.add_argument("--incognito")
options.add_argument("--disable-features=NetworkService")
options.add_argument("--disable-notifications")
driver = webdriver.Chrome(options=options)

try:
    # Navigate to the website
    driver.get("https://saucedemo.com/")
    time.sleep(5)  # wait for 5 seconds after opening the page

    # Maximize the browser window
    driver.maximize_window()

    # Login to the application
    driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys("standard_user")
    time.sleep(3)  # wait for 3 seconds
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("secret_sauce")
    time.sleep(3)  # wait for 3 seconds
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()

    # Wait and add 'Bike Light' to the cart
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))
    ).click()
    time.sleep(3)

    # Wait and add 'Fleece Jacket' to the cart
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))
    ).click()
    time.sleep(3)

    # Proceed to the cart
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a'))
    ).click()
    time.sleep(3)

    # Proceed to checkout
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="checkout"]'))
    ).click()
    time.sleep(3)

    # Enter checkout information
    driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys("Jonnathan")
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys("K")
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys("10007")
    time.sleep(3)

    # Continue to next checkout step
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="continue"]'))
    ).click()
    time.sleep(3)

    # Verify 'Payment Information' label is visible
    payment_info_card = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[1]'))
    )
    
    if payment_info_card.is_displayed():
        print("Test Passed: 'Payment Information' label is visible.")
        driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\success.png")
        sys.exit(0)
    else:
        print("Test Failed: 'Payment Information' label is not visible.")
        sys.exit(1)

except Exception as e:
    print(f"Test Failed: {str(e)}")
    driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\error.png")
    sys.exit(1)

finally:
    # Quit the driver
    driver.quit()
