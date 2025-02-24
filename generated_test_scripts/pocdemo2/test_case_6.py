
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time

def test_ui():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-notifications')
    options.add_argument('--incognito')
    options.add_argument('--disable-features=NetworkService')
    
    driver = webdriver.Chrome(options=options)
    try:
        driver.maximize_window()
        driver.get("https://practicetestautomation.com/")
        time.sleep(5)

        time.sleep(3)

        courses_menu = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Courses')]"))
        )
        courses_menu.click()

        time.sleep(3)

        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://practicetestautomation.com/courses/")
        )

        if driver.current_url == "https://practicetestautomation.com/courses/":
            sys.exit(0)
        else:
            sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
    finally:
        driver.quit()

test_ui()
