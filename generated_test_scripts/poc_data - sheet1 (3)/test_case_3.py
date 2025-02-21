
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def test_invalid_login():
    options = Options()
    options.headless = True
    options.add_argument('--disable-notifications')
    options.add_argument('--disable-popup-blocking')
    options.add_argument('--incognito')

    driver = webdriver.Chrome(options=options)
    
    try:
        # Open the page
        driver.get('http://example.com/login')
        time.sleep(5)  # Wait for 5 secs after opening the page

        # Maximize the page
        driver.maximize_window()

        # Wait for 3 secs before every action
        time.sleep(3)

        # Enter the username: 'student'
        username_field = driver.find_element(By.XPATH, "//input[@name='username']")
        username_field.send_keys('student')

        time.sleep(3)

        # Enter the invalid password: 'incorrectPassword'
        password_field = driver.find_element(By.XPATH, "//input[@name='password']")
        password_field.send_keys('incorrectPassword')

        time.sleep(3)

        # Click submit
        submit_button = driver.find_element(By.XPATH, "//*[@id='submit']")
        submit_button.click()

        time.sleep(3)

        # Verify error message for invalid password
        error_message = None
        try:
            error_message = driver.find_element(By.XPATH, "//div[@id='error']")
        except:
            pass
        
        if error_message and "invalid" in error_message.text.lower():
            print("Test Case Passed")
            driver.quit()
            exit(0)
        else:
            print("Test Case Failed")
            driver.quit()
            exit(1)

    except Exception as e:
        print(f"Exception occurred: {e}")
        driver.quit()
        exit(1)

test_invalid_login()
