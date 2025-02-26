
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time

def test_homepage_navigation():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--incognito")
    options.add_argument("--disable-features=NetworkService")
    options.add_argument("--disable-notifications")
    
    driver = webdriver.Chrome(options=options)
    
    try:
        # Open the homepage
        driver.get("https://practicetestautomation.com/")
        time.sleep(5)
        driver.maximize_window()
        time.sleep(3)

        # Click on the "Home" menu
        home_menu = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Home')]"))
        )
        home_menu.click()
        time.sleep(3)

        # Wait for the page to load and verify the URL
        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://practicetestautomation.com/")
        )
        current_url = driver.current_url
        
        if current_url == "https://practicetestautomation.com/":
            sys.exit(0)
        else:
            sys.exit(1)
    except Exception as e:
        sys.exit(1)
    finally:
        driver.quit()

if __name__ == "__main__":
    test_homepage_navigation()
