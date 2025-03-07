
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from compare_sentences import compare_sentences

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-popup-blocking")

# Initialize WebDriver
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

try:
    # Navigate to the SauceDemo login page
    driver.get("https://www.saucedemo.com")

    # Wait and enter username
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='user-name']"))
    )
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard_user")

    # Wait and enter password
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='password']"))
    )
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")

    # Wait and click the login button
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='login-button']"))
    )
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@id='login-button']").click()

    # Wait and assert the title of the product listing page
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[@data-test='title']"))
    )
    time.sleep(3)
    product_page_title = driver.find_element(By.XPATH, "//span[@data-test='title']").text
    assert compare_sentences(product_page_title, "Products")

    # Wait and add Sauce Labs Backpack to the cart
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']"))
    )
    time.sleep(3)
    driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']").click()

    # Wait and navigate to the shopping cart
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[@class='shopping_cart_link']"))
    )
    time.sleep(3)
    driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()

    # Wait and verify the product is in the cart
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='inventory_item_name' and text()='Sauce Labs Backpack']"))
    )

    # Wait and remove the Sauce Labs Backpack from the cart
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[@id='remove-sauce-labs-backpack']"))
    )
    time.sleep(3)
    driver.find_element(By.XPATH, "//button[@id='remove-sauce-labs-backpack']").click()

    # Wait to confirm that the cart is empty
    try:
        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='inventory_item_name' and text()='Sauce Labs Backpack']"))
        )
        sys.exit(1)
    except:
        pass

    print("Test case passed")
    sys.exit(0)

except Exception as e:
    print(f"Test case failed: {e}")
    sys.exit(1)

finally:
    driver.quit()
