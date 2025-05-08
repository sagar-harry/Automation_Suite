
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-features=NetworkService")

try:
    # Initialize the WebDriver
    driver = webdriver.Chrome(options=chrome_options)

    # Maximize the window and open the URL
    driver.maximize_window()
    driver.get("http://example.com")  # Replace with actual URL
    
    # Wait for 5 seconds
    time.sleep(5)

    # Wait for the username field to appear
    wait = WebDriverWait(driver, 10)
    username_field = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/form/p[1]")))

    # Enter the username
    time.sleep(3)
    username_field.send_keys("testqa999@gmail.com")

    # Wait for the password field to appear
    password_field = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/form/p[2]")))

    # Enter the password
    time.sleep(3)
    password_field.send_keys("abcd123")

    # Wait for the submit button to appear
    submit_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='submit']")))

    # Click the submit button
    time.sleep(3)
    submit_button.click()

    # Assuming a successful login redirects to a new page, check that page has loaded
    # Adjust the XPath or condition below based on your application's specific successful login criteria
    wait.until(EC.title_contains("Dashboard"))

    # Save the snapshot of the page
    driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\screenshot.png")

    # End with exit code 0 for success
    sys.exit(0)

except Exception as e:
    # Save the snapshot of the page on failure as well
    driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\screenshot_failed.png")
    print(f"Test failed: {e}")

    # End with exit code 1 for failure
    sys.exit(1)

finally:
    # Ensure the browser is closed in case of any failure
    driver.quit()
