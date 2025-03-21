
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

def test_complete_purchase_flow():
    # Chrome Options
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-features=NetworkService")
    
    # Initialize WebDriver
    driver = webdriver.Chrome(options=chrome_options)
    
    try:
        # Open website
        driver.get("https://saucedemo.com/")
        time.sleep(5)
        driver.maximize_window()
        
        # Log in
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="user"]'))).send_keys("standard")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="password"]'))).send_keys("secret_sauce")
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="login-button"]'))).click()
        time.sleep(3)

        # Add items to cart
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))).click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))).click()
        time.sleep(3)

        # Go to cart and checkout
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="123"]/a'))).click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="checkout"]'))).click()
        time.sleep(3)
        
        # Enter checkout information
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="first-name"]'))).send_keys("Jonnathan")
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="last-name"]'))).send_keys("K")
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="postal-code"]'))).send_keys("10007")
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="continue"]'))).click()
        time.sleep(3)

        # Complete the purchase
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="finish"]'))).click()
        time.sleep(3)

        # Return to homepage and logout
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="back-to-products"]'))).click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-burger-menu-btn"]'))).click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="logout_sidebar_link"]'))).click()
        time.sleep(3)

        # Screenshot the page
        driver.save_screenshot('C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\final_page.png')

        sys.exit(0)

    except Exception as e:
        driver.save_screenshot('C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\error.png')
        sys.exit(1)

    finally:
        driver.quit()

if __name__ == "__main__":
    test_complete_purchase_flow()
