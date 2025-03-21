
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def main():
    try:
        options = Options()
        options.add_argument("--incognito")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-popups")
        options.add_argument("--disable-features=NetworkService")

        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.get("https://saucedemo.com/")
        time.sleep(5)

        wait = WebDriverWait(driver, 20)

        # Login
        from LoginPage import login
        login(driver, "standard_user", "secret_sauce", wait)

        # Add Bike Light to Cart
        bike_light = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='add-to-cart-sauce-labs-bike-light']")))
        bike_light.click()
        time.sleep(3)

        # Add Fleece Jacket to Cart
        fleece_jacket = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='add-to-cart-sauce-labs-fleece-jacket']")))
        fleece_jacket.click()
        time.sleep(3)

        # Check Cart Count
        cart_count = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='shopping_cart_container']/a/span")))
        assert cart_count.text == '2'
        time.sleep(3)

        # Remove Bike Light from Cart
        remove_bike_light = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='remove-sauce-labs-bike-light']")))
        remove_bike_light.click()
        time.sleep(3)

        # Remove Fleece Jacket from Cart
        remove_fleece_jacket = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='remove-sauce-labs-fleece-jacket']")))
        remove_fleece_jacket.click()
        time.sleep(3)

        # Check for absence of Cart Count
        assert len(driver.find_elements(By.XPATH, "//*[@id='shopping_cart_container']/a/span")) == 0
        time.sleep(3)

        # Add Bolt T-Shirt to Cart
        bolt_tshirt = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='add-to-cart-sauce-labs-bolt-t-shirt']")))
        bolt_tshirt.click()
        time.sleep(3)

        # Check Cart Count
        cart_count = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='shopping_cart_container']/a/span")))
        assert cart_count.text == '1'
        time.sleep(3)

        # Save screenshot
        driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\final_state.png")

        driver.quit()
        sys.exit(0)

    except Exception as e:
        driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\error_state.png")
        driver.quit()
        sys.exit(1)

if __name__ == "__main__":
    main()
