
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-features=NetworkService")

driver = webdriver.Chrome(options=chrome_options)

try:
    # Open website
    driver.get("https://saucedemo.com/")
    time.sleep(5)
    driver.maximize_window()

    # Perform login
    def login():
        username = driver.find_element(By.XPATH, '//*[@id="user"]')
        password = driver.find_element(By.XPATH, '//*[@id="password"]')
        login_button = driver.find_element(By.XPATH, '//*[@id="login-button"]')

        username.send_keys("standard")
        time.sleep(3)
        password.send_keys("secret_sauce")
        time.sleep(3)
        login_button.click()

    login()

    # Adding items to cart
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))).click()
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))).click()
    time.sleep(3)

    # Checkout process
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="123"]/a'))).click()
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="checkout"]'))).click()
    time.sleep(3)

    # Enter user details
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="first-name"]'))).send_keys("Jonnathan")
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="last-name"]'))).send_keys("K")
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="postal-code"]'))).send_keys("10007")
    time.sleep(3)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="continue"]'))).click()
    time.sleep(3)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="finish"]'))).click()
    time.sleep(3)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="back-to-products"]'))).click()
    time.sleep(3)

    # Logout process
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-burger-menu-btn"]'))).click()
    time.sleep(3)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="logout_sidebar_link"]'))).click()
    time.sleep(3)

    # Save the snapshot of the final page
    driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png")

    sys.exit(0)

except Exception as e:
    print(f"Test failed: {e}")
    driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\failure_screenshot.png")
    sys.exit(1)

finally:
    driver.quit()
