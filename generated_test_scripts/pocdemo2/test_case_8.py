
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_ui_scenario():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--incognito")
    options.add_argument("--disable-features=NetworkService")
    
    driver = webdriver.Chrome(options=options)
    try:
        driver.maximize_window()
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")
        time.sleep(5)
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Contact')]"))
        )
        time.sleep(3)

        contact_menu = driver.find_element(By.XPATH, "//a[contains(text(),'Contact')]")
        contact_menu.click()
        time.sleep(3)

        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://practicetestautomation.com/contact/")
        )

        if driver.current_url == "https://practicetestautomation.com/contact/":
            sys.exit(0)
        else:
            sys.exit(1)

    except Exception as e:
        sys.exit(1)
    finally:
        driver.quit()

if __name__ == "__main__":
    test_ui_scenario()
