
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

try:
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-features=NetworkService")
    
    driver = webdriver.Chrome(options=options)
    
    driver.maximize_window()
    
    driver.get("https://practicetestautomation.com/")
    time.sleep(3)
    
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Home')]"))).click()
    time.sleep(3)
    
    current_url = driver.current_url
    
    time.sleep(3)
    
    if current_url == "https://practicetestautomation.com/":
        sys.exit(0)
    else:
        sys.exit(1)

finally:
    driver.quit()
