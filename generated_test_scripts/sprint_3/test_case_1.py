
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import sys

def test_purchase_flow():
    try:
        # Set up Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-popups")
        chrome_options.add_argument("--disable-features=NetworkService")

        # Initialize WebDriver
        driver = webdriver.Chrome(options=chrome_options)
        
        # Maximize browser window
        driver.maximize_window()

        # Open the login page
        driver.get("https://saucedemo.com/")
        time.sleep(5)

        # Login
        username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="user"]')))
        password = driver.find_element(By.XPATH, '//*[@id="password"]')
        login_button = driver.find_element(By.XPATH, '//*[@id="login-button"]')

        username.send_keys("standard")
        time.sleep(3)
        password.send_keys("secret_sauce")
        time.sleep(3)
        login_button.click()
        
        # Add products to the cart
        bike_light = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')))
        fleece_jacket = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')

        bike_light.click()
        time.sleep(3)
        fleece_jacket.click()
        time.sleep(3)
        
        # Navigate to cart and checkout
        cart_icon = driver.find_element(By.XPATH, '//*[@id="123"]/a')
        cart_icon.click()
        time.sleep(3)

        checkout = driver.find_element(By.XPATH, '//*[@id="checkout"]')
        checkout.click()
        time.sleep(3)

        # Enter checkout information
        first_name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="first-name"]')))
        last_name = driver.find_element(By.XPATH, '//*[@id="last-name"]')
        postal_code = driver.find_element(By.XPATH, '//*[@id="postal-code"]')

        first_name.send_keys("Jonnathan")
        time.sleep(3)
        last_name.send_keys("K")
        time.sleep(3)
        postal_code.send_keys("10007")
        time.sleep(3)

        continue_button = driver.find_element(By.XPATH, '//*[@id="continue"]')
        continue_button.click()
        time.sleep(3)

        # Complete purchase
        finish = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="finish"]')))
        finish.click()
        time.sleep(3)
        
        # Return to homepage
        back_to_products = driver.find_element(By.XPATH, '//*[@id="back-to-products"]')
        back_to_products.click()
        time.sleep(3)

        # Logout
        logout_sidebar = driver.find_element(By.XPATH, '//*[@id="react-burger-menu-btn"]')
        logout_sidebar.click()
        time.sleep(3)

        logout_button = driver.find_element(By.XPATH, '//*[@id="logout_sidebar_link"]')
        logout_button.click()
        time.sleep(3)

        # Save snapshot of page
        driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\final_state.png")

        # Exit with code 0 indicating success
        driver.quit()
        sys.exit(0)

    except TimeoutException as e:
        driver.quit()
        sys.exit(1)
    except Exception as e:
        driver.quit()
        sys.exit(1)

# Execute the test
test_purchase_flow()
