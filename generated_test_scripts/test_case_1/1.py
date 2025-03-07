
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from compare_sentences import compare_sentences

def test_successful_login():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--incognito")

    driver = webdriver.Chrome(options=options)
    try:
        # Step 1: Given the user is on the Login Page ("https://www.saucedemo.com/")
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        sleep(3)

        # Step 2: And the login form is present with "Username" and "Password" fields
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@data-test='username']")))
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@data-test='password']")))

        # Step 3: When the user enters "standard_user" in the "Username" field
        driver.find_element(By.XPATH, "//input[@data-test='username']").send_keys("standard_user")
        sleep(3)

        # Step 4: And the user enters "secret_sauce" in the "Password" field
        driver.find_element(By.XPATH, "//input[@data-test='password']").send_keys("secret_sauce")
        sleep(3)

        # Step 5: And the user clicks the "Login" button
        driver.find_element(By.XPATH, "//input[@data-test='login-button']").click()
        sleep(3)

        # Step 6: Then the user should be redirected to the Product Listing Page ("/inventory.html")
        WebDriverWait(driver, 10).until(EC.url_contains("/inventory.html"))
        
        # Step 7: And the Products title "Products" should be displayed
        products_title_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@data-test='title']"))
        )
        products_title_text = products_title_element.text.strip()
        expected_title = "Products"
        
        if compare_sentences(products_title_text, expected_title):
            print("Test Passed")
            sys.exit(0)
        else:
            print("Test Failed")
            sys.exit(1)

    except Exception as e:
        print(f"Test Failed due to an exception: {e}")
        sys.exit(1)

    finally:
        driver.quit()

if __name__ == "__main__":
    test_successful_login()
