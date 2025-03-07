
import sys
import time
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
wait = WebDriverWait(driver, 10)

try:
    # Navigate to the home page
    driver.get("https://www.saucedemo.com")
    
    # Maximize the page
    driver.maximize_window()

    # Wait for 3 seconds
    time.sleep(3)
    
    # Given the user is on the login page
    username_field = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@data-test='username']")))
    password_field = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@data-test='password']")))
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@data-test='login-button']")))

    # When the user enters username "standard_user"
    username_field.send_keys("standard_user")
    time.sleep(3)

    # And the user enters password "secret_sauce"
    password_field.send_keys("secret_sauce")
    time.sleep(3)

    # And the user clicks on the login button
    login_button.click()
    time.sleep(3)

    # Then the user should be navigated to the product listing page
    product_listing_title = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@data-test='title' and text()='Products']")))

    # Assert the title
    if compare_sentences(product_listing_title.text, "Products"):
        print("Test case passed: User successfully navigated to the product listing page.")
        sys.exit(0)
    else:
        print("Test case failed: User did not navigate to the product listing page.")
        sys.exit(1)

except Exception as e:
    print(f"Test case failed due to an exception: {str(e)}")
    sys.exit(1)
finally:
    # Close the driver
    driver.quit()
