
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-features=NetworkService")

    # Initialize WebDriver
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get("https://saucedemo.com/")
    time.sleep(5)

    # Login
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="user-name"]'))).send_keys("standard_user")
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("secret_sauce")
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()

    # Add items to cart
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))).click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()

    # Proceed to cart
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()

    # Checkout
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="checkout"]'))).click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys("Jonnathan")
    driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys("K")
    driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys("10007")
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="continue"]').click()

    # Finish purchase
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="finish"]'))).click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="back-to-products"]').click()

    # Logout
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="react-burger-menu-btn"]'))).click()
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="logout_sidebar_link"]'))).click()

    # Screenshot
    driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\final_state.png")

    # Test passed
    sys.exit(0)

except Exception as e:
    print(f"Test failed: {e}")
    driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\error_state.png")
    sys.exit(1)

finally:
    driver.quit()
