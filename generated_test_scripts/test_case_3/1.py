
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import sys
from compare_sentences import compare_sentences

try:
    # Setup Chrome options to disable notifications and pop-ups, and run in incognito mode
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--incognito")

    # Initialize the WebDriver
    driver = webdriver.Chrome(options=chrome_options)
    
    # Maximize the browser window and visit the base URL
    driver.maximize_window()
    driver.get("https://saucedemo.com/")

    # Wait for 3 seconds before each action
    sleep(3)

    # Login to SauceDemo
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@data-test='username']"))
    ).send_keys("standard_user")
    sleep(3)

    driver.find_element(By.XPATH, "//input[@data-test='password']").send_keys("secret_sauce")
    sleep(3)
    
    driver.find_element(By.XPATH, "//input[@data-test='login-button']").click()

    # Verify redirection to the product listing page
    sleep(3)
    if "/inventory.html" not in driver.current_url:
        raise AssertionError("Not redirected to /inventory.html")

    # Add a product to cart and proceed to cart
    driver.find_element(By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-backpack']").click()
    sleep(3)
    
    driver.find_element(By.XPATH, "//a[@data-test='shopping-cart-link']").click()
    sleep(3)

    # Verify "Your Cart" title presence
    cart_title = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//span[@data-test='title' and text()='Your Cart']"))
    ).text
    if not compare_sentences(cart_title, "Your Cart"):
        raise AssertionError("Title 'Your Cart' not found on Cart page")

    # Proceed to checkout
    driver.find_element(By.XPATH, "//button[@data-test='checkout']").click()
    sleep(3)

    # Verify redirection to checkout step-1 page
    if "/checkout-step-one.html" not in driver.current_url:
        raise AssertionError("Not redirected to /checkout-step-one.html")

    # Fill in user details and proceed to checkout step-2
    driver.find_element(By.XPATH, "//input[@data-test='firstName']").send_keys("Test")
    sleep(3)
    driver.find_element(By.XPATH, "//input[@data-test='lastName']").send_keys("User")
    sleep(3)
    driver.find_element(By.XPATH, "//input[@data-test='postalCode']").send_keys("12345")
    sleep(3)

    driver.find_element(By.XPATH, "//input[@data-test='continue']").click()
    sleep(3)

    # Verify redirection to checkout step-2 page
    if "/checkout-step-two.html" not in driver.current_url:
        raise AssertionError("Not redirected to /checkout-step-two.html")

    # Check order summary and finish the order
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'cart_list')]"))
    )
    finish_button_present = driver.find_element(By.XPATH, "//button[@data-test='finish']").is_displayed()
    if not finish_button_present:
        raise AssertionError("'Finish' button not present on checkout-step-two.html page")

    driver.find_element(By.XPATH, "//button[@data-test='finish']").click()
    sleep(3)

    # Verify redirection to the order confirmation page
    if "/checkout-complete.html" not in driver.current_url:
        raise AssertionError("Not redirected to /checkout-complete.html")

    # Verify order complete message
    order_confirmation_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h2[@data-test='complete-header' and text()='Thank you for your order!']"))
    ).text
    if not compare_sentences(order_confirmation_message, "Thank you for your order!"):
        raise AssertionError("Order confirmation message not found")

    print("Test Case Passed")
    sys.exit(0)

except Exception as e:
    print(f"Test Case Failed: {e}")
    sys.exit(1)

finally:
    # Close the browser
    driver.quit()
