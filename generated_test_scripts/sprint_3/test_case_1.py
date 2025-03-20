
import time
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login(driver, username, password):
    driver.find_element(By.XPATH, '//*[@id="user"]').send_keys(username)
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()

try:
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-features=NetworkService")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)

    driver.get("https://saucedemo.com/")
    time.sleep(5)  # Wait for 5 seconds after page open
    driver.maximize_window()

    login(driver, "standard", "secret_sauce")

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))
    )
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
    time.sleep(3)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))
    )
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
    time.sleep(3)

    driver.find_element(By.XPATH, '//*[@id="123"]/a').click()
    time.sleep(3)

    driver.find_element(By.XPATH, '//*[@id="checkout"]').click()
    time.sleep(3)

    driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys('Jonnathan')
    driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys('K')
    driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys('10007')

    driver.find_element(By.XPATH, '//*[@id="continue"]').click()
    time.sleep(3)

    driver.find_element(By.XPATH, '//*[@id="finish"]').click()
    time.sleep(3)

    driver.find_element(By.XPATH, '//*[@id="back-to-products"]').click()
    time.sleep(3)

    driver.find_element(By.XPATH, '//*[@id="react-burger-menu-btn"]').click()
    time.sleep(3)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="logout_sidebar_link"]'))
    )
    driver.find_element(By.XPATH, '//*[@id="logout_sidebar_link"]').click()
    time.sleep(3)

    # Snapshot the page state before closing
    driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\screenshot.png")

    driver.quit()
    sys.exit(0)  # Test case passed

except Exception as e:
    driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\screenshot_error.png")
    driver.quit()
    sys.exit(1)  # Test case failed
