
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time

# Configure options for headless mode, disable notifications and pop-ups, incognito mode
options = Options()
options.headless = True
options.add_argument("--disable-notifications")
options.add_argument("--incognito")

try:
    # Initialize WebDriver
    driver = webdriver.Chrome(options=options)
    
    # Open the page
    driver.get("https://practicetestautomation.com/practice-test-login/")
    time.sleep(5)
    
    # Maximize the page
    driver.maximize_window()
    
    # Enter username
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@name='username']")))
    time.sleep(3)
    username_field = driver.find_element(By.XPATH, "//input[@name='username']")
    username_field.send_keys('student')
    
    # Enter password
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@name='password']")))
    time.sleep(3)
    password_field = driver.find_element(By.XPATH, "//input[@name='password']")
    password_field.send_keys('Password123')
    
    # Click submit
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='submit']")))
    time.sleep(3)
    submit_button = driver.find_element(By.XPATH, "//*[@id='submit']")
    submit_button.click()
    
    # Verify message
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='loop-container']/div/article/div[1]/h1")))
    time.sleep(3)
    message_box = driver.find_element(By.XPATH, "//*[@id='loop-container']/div/article/div[1]/h1")
    assert "Logged In Successfully" in message_box.text, "Message not found!"
    
    driver.quit()
    sys.exit(0)
    
except Exception as e:
    driver.quit()
    print(str(e))
    sys.exit(1)
