
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time

def test_blog_navigation():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument("--disable-features=NetworkService")

    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Navigate to homepage
        driver.get("https://practicetestautomation.com/")
        time.sleep(3)

        # Click on the "Blog" menu
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Blog')]"))
        )
        time.sleep(3)
        blog_menu = driver.find_element(By.XPATH, "//a[contains(text(),'Blog')]")
        blog_menu.click()

        # Wait for page to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(@class, 'elementor-widget-container')]"))
        )
        time.sleep(3)

        # Verify the URL
        if driver.current_url == "https://practicetestautomation.com/blog/":
            sys.exit(0)
        else:
            sys.exit(1)
    
    except Exception as e:
        print(e)
        sys.exit(1)

    finally:
        driver.quit()

test_blog_navigation()
