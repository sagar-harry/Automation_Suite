
import sys
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from compare_sentences import compare_sentences

def test_validate_cart_count():
    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--start-maximized")
    
    # Initialize WebDriver
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Step 1: Given I open the SauceDemo login page
        driver.get("https://www.saucedemo.com")
        
        # Step 2: When I enter "standard_user" as username
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@data-test='username']"))
        ).send_keys("standard_user")
        sleep(3)
        
        # Step 3: And I enter "secret_sauce" as password
        driver.find_element(By.XPATH, "//*[@data-test='password']").send_keys("secret_sauce")
        sleep(3)
        
        # Step 4: And I click the "Login" button
        driver.find_element(By.XPATH, "//*[@data-test='login-button']").click()
        
        # Step 5: Then I should be redirected to the Product Listing Page
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@data-test='header-container']"))
        )
        sleep(3)
        
        # Step 6: When I add a product to the cart by clicking "Add to cart" on "Sauce Labs Backpack"
        driver.find_element(By.XPATH, "//*[@data-test='add-to-cart-sauce-labs-backpack']").click()
        sleep(3)
        
        # Step 7: Then the cart count should increase to 1 in the header
        cart_count_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@data-test='shopping-cart-badge']"))
        )
        cart_count = cart_count_element.text
        sentence1 = "1"
        if compare_sentences(sentence1, cart_count):
            print("Test passed")
            sys.exit(0)
        else:
            print("Test failed: Cart count is not 1")
            sys.exit(1)

    except Exception as e:
        print(f"Test failed due to an exception: {str(e)}")
        sys.exit(1)

    finally:
        driver.quit()

test_validate_cart_count()
