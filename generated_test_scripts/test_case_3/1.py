
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import sys
from compare_sentences import compare_sentences

# Initialize ChromeOptions
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--start-maximized")

# Start the WebDriver
driver = webdriver.Chrome(options=chrome_options)

# Test case steps
try:
    # Step 1: Given the user is on the SauceDemo login page
    driver.get("https://saucedemo.com/")
    time.sleep(3)
  
    # Step 2: When the user enters valid username 'standard_user' and password 'secret_sauce'
    driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys('standard_user')
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys('secret_sauce')
    time.sleep(3)
  
    # Step 3: And clicks on the login button
    driver.find_element(By.XPATH, "//input[@id='login-button']").click()
    time.sleep(3)
  
    # Step 4: Then the user should be redirected to the Product Listing Page with URL '/inventory.html'
    assert '/inventory.html' in driver.current_url
  
    # Step 5: When the user adds a product to the cart and goes to the Shopping Cart Page
    driver.find_element(By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-backpack']").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//a[@data-test='shopping-cart-link']").click()
    time.sleep(3)
  
    # Step 6: And the user clicks on the checkout button
    driver.find_element(By.XPATH, "//button[@id='checkout']").click()
    time.sleep(3)
  
    # Step 7: Then the User should be taken to Checkout Step 1 with URL '/checkout-step-one.html'
    assert '/checkout-step-one.html' in driver.current_url
  
    # Step 8: When the user enters 'First Name', 'Last Name', and 'Zip/Postal Code' and clicks continue
    driver.find_element(By.XPATH, "//input[@data-test='firstName']").send_keys('First Name')
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@data-test='lastName']").send_keys('Last Name')
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@data-test='postalCode']").send_keys('12345')
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@type='submit' and @data-test='continue']").click()
    time.sleep(3)
  
    # Step 9: Then the user should be taken to Checkout Step 2 - Order Overview with URL '/checkout-step-two.html'
    assert '/checkout-step-two.html' in driver.current_url
  
    # Step 10: When the user clicks on the 'Finish' button
    driver.find_element(By.XPATH, "//button[@id='finish']").click()
    time.sleep(3)
  
    # Step 11: Then the user should see 'Thank you for your order' message and be on Order Confirmation Page with URL '/checkout-complete.html'
    assert '/checkout-complete.html' in driver.current_url
    
    # Verify the thank you message by using compare_sentences function
    thank_you_message = driver.find_element(By.XPATH, "//h2[@class='complete-header' and text()='Thank you for your order!']").text
    assert compare_sentences(thank_you_message, "Thank you for your order!")  

    print("Test case passed")
    sys.exit(0)

except Exception as e:
    print(f"Test case failed due to: {e}")
    sys.exit(1)

finally:
    driver.quit()
