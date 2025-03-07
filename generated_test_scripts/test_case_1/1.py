
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from compare_sentences import compare_sentences

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-notifications")

# Initialize WebDriver
driver = webdriver.Chrome(options=chrome_options)

try:
    # Step 1: Open the Login Page
    driver.get("https://www.saucedemo.com")
    driver.maximize_window()
    time.sleep(3)

    # Define explicit wait
    wait = WebDriverWait(driver, 10)

    # Step 2: Enter the username
    username_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='user-name']")))
    username_input.send_keys("standard_user")
    time.sleep(3)
    
    # Step 3: Enter the password
    password_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='password']")))
    password_input.send_keys("secret_sauce")
    time.sleep(3)

    # Step 4: Click the login button
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='login-button']")))
    login_button.click()
    time.sleep(3)

    # Step 5: Assert the redirection to the Product Listing Page
    wait.until(EC.url_contains("/inventory.html"))
    current_url = driver.current_url
    expected_url = "https://www.saucedemo.com/inventory.html"
    if current_url.endswith("/inventory.html"):
        assert compare_sentences(expected_url, current_url), f"Expected: {expected_url}, Found: {current_url}"
    else:
        raise AssertionError("Didn't redirect to the expected URL")

    # Step 6: Verify that the Product Title is displayed
    product_title = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@data-test='title'][contains(text(),'Products')]")))
    assert compare_sentences(product_title.text, "Products"), f"Expected title: Products, Found: {product_title.text}"

    # Step 7: Check for the list of products
    product_list = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@data-test='inventory-list']")))
    assert product_list.is_displayed(), "Product list is not visible"

    print("Test Passed")
    sys.exit(0)

except Exception as e:
    print(f"Test Failed: {e}")
    sys.exit(1)

finally:
    # Close the browser
    driver.quit()
