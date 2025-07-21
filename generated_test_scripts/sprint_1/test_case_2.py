
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-features=NetworkService")

try:
    # Initialize driver
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()

    # Open URL
    driver.get('https://saucedemo.com/')
    time.sleep(5)

    # Login
    class LoginPage:
        def login(self, username, password):
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@id='user-name']"))
            ).send_keys(username)
            time.sleep(3)
            driver.find_element(By.XPATH, "//input[@id='password']").send_keys(password)
            time.sleep(3)
            driver.find_element(By.XPATH, "//input[@id='login-button']").click()
            time.sleep(3)

    login_page = LoginPage()
    login_page.login('standard_user', 'secret_sauce')

    # Add products to cart
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']"))
    ).click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']").click()
    time.sleep(3)
    
    # Proceed to checkout
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//button[@id='checkout']").click()
    time.sleep(3)

    # Enter checkout information
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='first-name']"))
    ).send_keys('Jonnathan')
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@id='last-name']").send_keys('K')
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@id='postal-code']").send_keys('10007')
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@id='continue']").click()
    time.sleep(3)

    # Verify payment information visibility
    payment_info_label = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'Payment Information')]"))
    )
    
    if payment_info_label:
        driver.save_screenshot('C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\payment_info_visible.png')
        sys.exit(0)
    else:
        sys.exit(1)

except Exception as e:
    driver.save_screenshot('C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\error.png')
    sys.exit(1)

finally:
    driver.quit()
