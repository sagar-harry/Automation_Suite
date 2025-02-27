
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time

def test_blog_menu_navigation():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-notifications')
    options.add_argument('--disable-popup-blocking')
    options.add_argument('--incognito')
    options.add_argument('--disable-features=NetworkService')

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    try:
        driver.get("https://practicetestautomation.com/")
        time.sleep(5)

        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, f"//a[contains(text(),'Blog')]"))
        ).click()
        time.sleep(3)

        WebDriverWait(driver, 5).until(
            EC.url_to_be("https://practicetestautomation.com/blog/")
        )

        if driver.current_url == "https://practicetestautomation.com/blog/":
            sys.exit(0)
        else:
            sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
    finally:
        driver.quit()

if __name__ == "__main__":
    test_blog_menu_navigation()
