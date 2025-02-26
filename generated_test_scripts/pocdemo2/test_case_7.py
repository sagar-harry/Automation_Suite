
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_blog_navigation():
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-popups")
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--disable-features=NetworkService")

        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        
        driver.get("https://practicetestautomation.com/")
        time.sleep(5)  # Wait 5 secs after opening the page

        wait = WebDriverWait(driver, 10)
        time.sleep(3)  # Wait for 3 secs before performing an action
        blog_menu = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Blog')]")))
        blog_menu.click()

        time.sleep(3)  # Wait for 3 secs after clicking to ensure page loads

        wait.until(EC.url_matches("https://practicetestautomation.com/blog/"))
        
        if driver.current_url == "https://practicetestautomation.com/blog/":
            driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\blog_page.png")
            sys.exit(0)
        else:
            raise Exception("URL did not match the expected URL after clicking Blog menu.")

    except Exception as e:
        print(f"Test failed: {e}")
        driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\failure.png")
        sys.exit(1)

    finally:
        driver.quit()

test_blog_navigation()
