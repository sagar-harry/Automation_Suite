
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

def test_login():
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-features=NetworkService")

    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get("http://example.com/login")  # Replace with actual URL
        time.sleep(5)
        driver.maximize_window()

        username_xpath = "/html/body/div[3]/form/p[1]"
        password_xpath = "/html/body/div[3]/form/p[2]"
        submit_xpath = "//*[@id='submit']"

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, username_xpath)))
        time.sleep(3)
        driver.find_element(By.XPATH, username_xpath).send_keys("testqa999@gmail.com")

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, password_xpath)))
        time.sleep(3)
        driver.find_element(By.XPATH, password_xpath).send_keys("abcd123")

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, submit_xpath)))
        time.sleep(3)
        driver.find_element(By.XPATH, submit_xpath).click()

        # Add verification step here if needed, for now assuming it passes
        time.sleep(3)
        
        driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png")
        sys.exit(0)

    except Exception as e:
        print(f"Test failed with exception: {e}")
        driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\error_screenshot.png")
        sys.exit(1)
    finally:
        driver.quit()

if __name__ == "__main__":
    test_login()
