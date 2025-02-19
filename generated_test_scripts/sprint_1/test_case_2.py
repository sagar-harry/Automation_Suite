
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(username)
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="login-button"]').click()

def test_payment_information_label_visible():
    url = "https://saucedemo.com/"
    username = "standard_user"
    password = "secret_sauce"

    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-notifications')
    options.add_argument('--incognito')
    
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(5)
    driver.maximize_window()

    login_page = LoginPage(driver)
    login_page.login(username, password)

    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="checkout"]').click()
    
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys('somename')
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys('lastname')
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys('123456')
    
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="continue"]').click()
    
    time.sleep(3)
    payment_info_visible = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[1]').is_displayed()
    
    driver.quit()
    
    if payment_info_visible:
        exit(0)
    else:
        exit(1)

if __name__ == "__main__":
    test_payment_information_label_visible()
