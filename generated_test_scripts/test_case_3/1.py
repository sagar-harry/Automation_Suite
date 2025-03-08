
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from compare_sentences import compare_sentences

def main():
    options = Options()
    options.add_argument("--disable-notifications")
    options.add_argument("--incognito")
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://www.saucedemo.com/")
        time.sleep(3)

        # Login Page
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@data-test='username']"))
        )
        driver.find_element(By.XPATH, "//input[@data-test='username']").send_keys("standard_user")
        time.sleep(3)

        driver.find_element(By.XPATH, "//input[@data-test='password']").send_keys("secret_sauce")
        time.sleep(3)

        driver.find_element(By.XPATH, "//input[@data-test='login-button']").click()
        time.sleep(3)

        # Product Listing Page
        WebDriverWait(driver, 10).until(
            EC.url_contains("/inventory.html")
        )

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-backpack']"))
        )
        driver.find_element(By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-backpack']").click()
        time.sleep(3)

        driver.find_element(By.XPATH, "//a[@data-test='shopping-cart-link']").click()
        time.sleep(3)

        # Shopping Cart Page
        WebDriverWait(driver, 10).until(
            EC.url_contains("/cart.html")
        )
        
        driver.find_element(By.XPATH, "//button[@data-test='checkout']").click()
        time.sleep(3)

        # Checkout Step 1 Page
        WebDriverWait(driver, 10).until(
            EC.url_contains("/checkout-step-one.html")
        )

        driver.find_element(By.XPATH, "//input[@data-test='firstName']").send_keys("John")
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@data-test='lastName']").send_keys("Doe")
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@data-test='postalCode']").send_keys("12345")
        time.sleep(3)

        driver.find_element(By.XPATH, "//input[@data-test='continue']").click()
        time.sleep(3)

        # Checkout Step 2 Page
        WebDriverWait(driver, 10).until(
            EC.url_contains("/checkout-step-two.html")
        )

        item_total = driver.find_element(By.XPATH, "//div[@data-test='subtotal-label']").text
        tax_amount = driver.find_element(By.XPATH, "//div[@data-test='tax-label']").text
        total_amount = driver.find_element(By.XPATH, "//div[@data-test='total-label']").text
        time.sleep(3)

        finish_button = driver.find_element(By.XPATH, "//button[@data-test='finish']")
        assert finish_button.is_displayed(), "Finish button is not displayed"
        time.sleep(3)

        finish_button.click()
        time.sleep(3)

        # Order Confirmation Page
        WebDriverWait(driver, 10).until(
            EC.url_contains("/checkout-complete.html")
        )

        thank_you_message = driver.find_element(By.XPATH, "//h2[@data-test='complete-header']").text
        assert compare_sentences(thank_you_message, "Thank you for your order!")

        sys.exit(0)

    except Exception as e:
        print(f"Test failed: {e}")
        sys.exit(1)

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
