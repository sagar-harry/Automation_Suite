
import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from compare_sentences import compare_sentences

def validate_cart_count():
    # Disable notifications, pop ups and enable incognito mode
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    
    # Instantiate WebDriver
    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 10)

    try:
        # Maximize the browser window
        driver.maximize_window()

        # Step 1: Given I am on the Login Page
        driver.get("https://saucedemo.com")
        time.sleep(3)

        # Step 2: When I enter the username "standard_user"
        username_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='user-name']")))
        username_input.send_keys("standard_user")
        time.sleep(3)

        # Step 3: And I enter the password "secret_sauce"
        password_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='password']")))
        password_input.send_keys("secret_sauce")
        time.sleep(3)

        # Step 4: And I click the login button
        login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='login-button']")))
        login_button.click()
        time.sleep(3)

        # Step 5: Then I should be redirected to the Product Listing Page
        page_title = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@data-test='title']"))).text
        assert compare_sentences("Products", page_title), f"Expected page title 'Products', but got '{page_title}'"
        
        # Step 6: When I click the "Add to Cart" button on a product
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")))
        add_to_cart_button.click()
        time.sleep(3)

        # Step 7: Then the cart count should increase by one
        cart_icon = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@class='shopping_cart_link']")))
        cart_count = cart_icon.find_element(By.XPATH, "//span[@class='shopping_cart_badge']").text
        assert compare_sentences("1", cart_count), f"Expected cart count to be '1', but got '{cart_count}'"

        # If all assertions pass
        sys.exit(0)

    except Exception as e:
        print(str(e))
        sys.exit(1)

    finally:
        driver.quit()

if __name__ == "__main__":
    validate_cart_count()
