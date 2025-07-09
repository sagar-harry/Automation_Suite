
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

class LoginPage:
    def login(self, driver, username, password):
        driver.get("https://saucedemo.com/")
        time.sleep(5)
        driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys(username)
        driver.find_element(By.XPATH, "//input[@id='password']").send_keys(password)
        driver.find_element(By.XPATH, "//input[@id='login-button']").click()

def take_screenshot(driver, path):
    driver.save_screenshot(path)

try:
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})
    options.add_argument("--disable-features=NetworkService")

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    login_page = LoginPage()
    login_page.login(driver, "standard_user", "secret_sauce")

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']"))).click()
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']"))).click()
    time.sleep(3)
    cart_badge = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[@class='shopping_cart_badge']")))
    assert cart_badge.text == '2'

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@id='remove-sauce-labs-bike-light']"))).click()
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@id='remove-sauce-labs-fleece-jacket']"))).click()
    time.sleep(3)

    try:
        driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']")
        test_result = 1
    except:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']"))).click()
        time.sleep(3)
        cart_badge = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[@class='shopping_cart_badge']")))
        assert cart_badge.text == '1'
        test_result = 0

except Exception as e:
    test_result = 1
    take_screenshot(driver, "C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\error.png")
    print(e)

driver.quit()
sys.exit(test_result)
