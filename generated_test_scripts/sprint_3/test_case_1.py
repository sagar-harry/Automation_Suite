
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time

def test_login():
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popups")
    options.add_argument("--disable-features=NetworkService")

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    
    try:
        driver.get("https://example-login-page.com")
        time.sleep(5)

        username_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/form/p[1]"))
        )
        time.sleep(3)
        username_field.send_keys("testqa999@gmail.com")

        password_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/form/p[2]"))
        )
        time.sleep(3)
        password_field.send_keys("abcd123")

        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='submit']"))
        )
        time.sleep(3)
        submit_button.click()

        # Add logic to verify successful login, example:
        # success_message = WebDriverWait(driver, 10).until(
        #     EC.visibility_of_element_located((By.XPATH, "//div[@class='success']"))
        # )
        # assert success_message.is_displayed(), "Login success message not displayed."

        sys.exit(0)
        
    except Exception as e:
        driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\screenshot.png")
        sys.exit(1)

    finally:
        driver.quit()

if __name__ == "__main__":
    test_login()
