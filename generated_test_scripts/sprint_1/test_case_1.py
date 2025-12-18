
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

class LoginPage:
    def login(self, driver, username, password):
        driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys(username)
        driver.find_element(By.XPATH, "//input[@id='password']").send_keys(password)
        driver.find_element(By.XPATH, "//input[@id='login-button']").click()

def main():
    try:
        # Setup Chrome driver options
        options = webdriver.ChromeOptions()
        options.add_argument("--incognito")
        options.add_argument("--disable-features=NetworkService")
        options.add_argument("--disable-notifications")

        # Initialize the WebDriver
        driver = webdriver.Chrome(options=options)
        driver.get("https://saucedemo.com/")
        driver.maximize_window()
        time.sleep(5)

        # Login
        login_page = LoginPage()
        login_page.login(driver, "standard_user", "secret_sauce")
        time.sleep(3)

        # Add Bike Light and Fleece Jacket to the cart
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']"))).click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']"))).click()
        time.sleep(3)

        # Verify cart badge displays '2'
        cart_badge = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[@class='shopping_cart_badge']")))
        assert cart_badge.text == '2', "Cart Badge does not display '2'"

        # Remove Bike Light and Fleece Jacket
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='remove-sauce-labs-bike-light']"))).click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='remove-sauce-labs-fleece-jacket']"))).click()
        time.sleep(3)

        # Verify cart badge does not exist
        cart_badge_elements = driver.find_elements(By.XPATH, "//span[@class='shopping_cart_badge']")
        assert len(cart_badge_elements) == 0, "Cart Badge still exists"

        # Add Bolt T-Shirt to the cart
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']"))).click()
        time.sleep(3)

        # Verify cart badge displays '1'
        cart_badge = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[@class='shopping_cart_badge']")))
        assert cart_badge.text == '1', "Cart Badge does not display '1'"

        # Save page snapshot
        driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\test_case.png")
        
        # Close the browser
        driver.quit()

        # Test case passed
        sys.exit(0)

    except Exception as e:
        # Save page snapshot for failures
        driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\error.png")
        driver.quit()
        sys.exit(1)

if __name__ == "__main__":
    main()
