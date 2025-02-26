
import sys
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("--incognito")
options.add_argument("--disable-notifications")
options.add_argument("--disable-features=NetworkService")

try:
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://saucedemo.com/")
    sleep(5)

    # Login
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="user-name"]')))
    driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys("standard_user")
    sleep(3)
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("secret_sauce")
    sleep(3)
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()

    # Add items to cart
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')))
    sleep(3)
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
    sleep(3)
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()

    # Proceed to cart and checkout
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a')))
    sleep(3)
    driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
    sleep(3)
    driver.find_element(By.XPATH, '//*[@id="checkout"]').click()

    # Fill checkout information
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="first-name"]')))
    driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys("somename")
    sleep(3)
    driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys("lastname")
    sleep(3)
    driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys("123456")
    sleep(3)
    driver.find_element(By.XPATH, '//*[@id="continue"]').click()

    # Complete purchase
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="finish"]')))
    sleep(3)
    driver.find_element(By.XPATH, '//*[@id="finish"]').click()

    # Back to home and logout
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="back-to-products"]')))
    sleep(3)
    driver.find_element(By.XPATH, '//*[@id="back-to-products"]').click()
    sleep(3)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-burger-menu-btn"]')))
    driver.find_element(By.XPATH, '//*[@id="react-burger-menu-btn"]').click()
    sleep(3)
    driver.find_element(By.XPATH, '//*[@id="logout_sidebar_link"]').click()

    # Successful test
    driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\test_script.png")
    sys.exit(0)

except Exception as e:
    driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\test_script.png")
    sys.exit(1)

finally:
    driver.quit()
