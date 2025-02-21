
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def test_login_error():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-notifications')
    options.add_argument('--incognito')

    driver = webdriver.Chrome(options=options)

    try:
        # Open the page
        driver.get("https://practicetestautomation.com/practice-test-login/")
        time.sleep(5)
        driver.maximize_window()
        
        # Finding elements with wait
        driver.implicitly_wait(10)
        
        # Enter the username
        username_field = driver.find_element(By.XPATH, "//input[@name='username']")
        time.sleep(3)
        username_field.send_keys("incorrectUser")
        
        # Enter the password
        password_field = driver.find_element(By.XPATH, "//input[@name='password']")
        time.sleep(3)
        password_field.send_keys("Password123")
        
        # Click submit
        submit_button = driver.find_element(By.XPATH, "//*[@id='submit']")
        time.sleep(3)
        submit_button.click()
        
        # Verify error message
        error_message = driver.find_element(By.XPATH, "//*[@id='error']")
        time.sleep(3)
        assert error_message.text == "Your username is invalid!"
        print("Test passed.")
        exit(0)
        
    except Exception as e:
        print(f"Test failed: {e}")
        exit(1)
        
    finally:
        driver.quit()

if __name__ == "__main__":
    test_login_error()
