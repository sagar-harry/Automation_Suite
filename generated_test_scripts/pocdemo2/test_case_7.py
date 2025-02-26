
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

options = Options()
options.add_argument("--headless=new")
options.add_argument("--disable-notifications")
options.add_argument("--incognito")
options.add_argument("--disable-features=NetworkService")

driver = webdriver.Chrome(options=options)

try:
    # Navigate to the homepage
    driver.get("https://practicetestautomation.com/")
    driver.maximize_window()
    time.sleep(5)

    # Wait for 3 secs before clicking the "Blog" menu
    time.sleep(3)
    
    # Click on the "Blog" menu
    blog_menu = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Blog')]"))
    )
    blog_menu.click()
    
    # Wait for 3 secs after clicking Blog menu
    time.sleep(3)

    # Wait for the blog page to load and verify the URL
    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://practicetestautomation.com/blog/")
    )

    if driver.current_url == "https://practicetestautomation.com/blog/":
        sys.exit(0)
    else:
        sys.exit(1)

except Exception as e:
    sys.exit(1)
finally:
    driver.quit()
