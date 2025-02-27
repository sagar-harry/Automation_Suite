
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

def run_test():
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-features=NetworkService")
        
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        
        driver.get("https://practicetestautomation.com/")
        time.sleep(5)
        
        wait = WebDriverWait(driver, 10)
        time.sleep(3)
        
        courses_menu = wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Courses')]")))
        courses_menu.click()
        time.sleep(3)
        
        wait.until(EC.url_to_be("https://practicetestautomation.com/courses/"))
        
        # Test passed
        sys.exit(0)
    except Exception as e:
        print(f"Test failed: {e}")
        sys.exit(1)
    finally:
        driver.quit()

if __name__ == "__main__":
    run_test()
