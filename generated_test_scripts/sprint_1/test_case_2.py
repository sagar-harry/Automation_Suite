
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(username)
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        self.driver.find_element(By.XPATH, '//*[@id="login-button"]').click()

def main():
    # Setup Chrome options
    chrome_options = Options()
    chrome_options.headless = True
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--incognito")

    try:
        # Initialize the Chrome driver
        driver = webdriver.Chrome(options=chrome_options)

        # Open the website
        driver.get("https://saucedemo.com/")
        
        # Wait for page to load
        sleep(5)

        # Maximize window
        driver.maximize_window()

        # Login to system
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")
        sleep(3)

        # Add 'Bike Light' to the cart
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
        sleep(3)

        # Add 'Fleece Jacket' to the cart
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
        sleep(3)

        # Proceed to Cart
        driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
        sleep(3)
        
        # Checkout
        driver.find_element(By.XPATH, '//*[@id="checkout"]').click()
        sleep(3)

        # Enter Checkout Information
        driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys("somename")
        driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys("lastname")
        driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys("123456")
        sleep(3)

        # Continue to Payment Information
        driver.find_element(By.XPATH, '//*[@id="continue"]').click()
        sleep(3)

        # Assert Payment Information is displayed
        payment_info = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[1]')
        assert payment_info.is_displayed(), "Payment Information is not visible."

        # Exit with code 0 if test case passed
        print("Test passed")
        exit(0)

    except Exception as e:
        # Exit with code 1 if test case failed
        print(f"Test failed: {str(e)}")
        exit(1)

    finally:
        # Quit the driver
        driver.quit()

if __name__ == "__main__":
    main()
