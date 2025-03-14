
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    url = "https://saucedemo.com/"
    username = "standard_user"
    password = "secret_sauce"

    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-features=NetworkService")

    driver = webdriver.Chrome(options=chrome_options)
    
    driver.get(url)
    time.sleep(5)
    driver.maximize_window()
    time.sleep(3)

    # Login
    driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(username)
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
    time.sleep(3)

    # Add items to cart
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))).click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
    time.sleep(3)
    
    # Navigate to cart
    driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
    time.sleep(3)

    # Proceed to checkout
    driver.find_element(By.XPATH, '//*[@id="checkout"]').click()
    time.sleep(3)
    
    # Enter checkout information
    driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys("Jonnathan")
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys("K")
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys("10007")
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="continue"]').click()
    time.sleep(3)
    
    # Complete the purchase
    driver.find_element(By.XPATH, '//*[@id="finish"]').click()
    time.sleep(3)
    
    # Return to the homepage
    driver.find_element(By.XPATH, '//*[@id="back-to-products"]').click()
    time.sleep(3)

    # Logout
    driver.find_element(By.XPATH, '//*[@id="react-burger-menu-btn"]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="logout_sidebar_link"]').click()

    driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\screenshot.png")

    sys.exit(0)

except Exception as e:
    driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\error_screenshot.png")
    sys.exit(1)
finally:
    driver.quit()
