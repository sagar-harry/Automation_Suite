
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

def test_contact_page_navigation():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--incognito")
    options.add_argument("--disable-features=NetworkService")

    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")
        time.sleep(5)
        driver.maximize_window()

        time.sleep(3)
        contact_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Contact')]"))
        )
        contact_link.click()

        time.sleep(3)
        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://practicetestautomation.com/contact/")
        )

        current_url = driver.current_url
        if current_url == "https://practicetestautomation.com/contact/":
            sys.exit(0)
        else:
            sys.exit(1)

    except Exception as e:
        print(f"Test failed due to an exception: {e}")
        sys.exit(1)

    finally:
        driver.quit()

if __name__ == "__main__":
    test_contact_page_navigation()
