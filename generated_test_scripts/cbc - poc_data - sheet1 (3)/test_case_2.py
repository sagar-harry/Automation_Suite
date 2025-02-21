
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def run_test():
    chrome_options = Options()
    chrome_options.headless = True
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-features=NetworkService")
    
    try:
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://practicetestautomation.com/practice-test-login/")
        
        time.sleep(5)  # Wait for 5 secs after page opens
        driver.maximize_window()
        
        # Wait for page elements
        time.sleep(3)
        
        # Find and interact with input fields
        username_field = driver.find_element(By.XPATH, "//input[@name='username']")
        password_field = driver.find_element(By.XPATH, "//input[@name='password']")
        submit_button = driver.find_element(By.XPATH, "//*[@id='submit']")
        
        # Input username
        time.sleep(3)
        username_field.send_keys("incorrectUser")
        
        # Input password
        time.sleep(3)
        password_field.send_keys("Password123")
        
        # Click submit button
        time.sleep(3)
        submit_button.click()
        
        # Verify error message
        time.sleep(3)
        error_message = driver.find_element(By.XPATH, "//*[@id='error']").text
        assert error_message.lower() == "your username is invalid!"
        
        driver.quit()
        exit(0)
    
    except Exception as e:
        print(f"Test failed: {e}")
        driver.quit()
        exit(1)

if __name__ == "__main__":
    run_test()
