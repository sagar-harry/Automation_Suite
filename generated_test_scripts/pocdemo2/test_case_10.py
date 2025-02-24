
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import sys

def run_test():
    # Set up Chrome options
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-notifications')
    options.add_argument('--incognito')
    options.add_argument('--disable-features=NetworkService')

    # Initialize WebDriver
    driver = webdriver.Chrome(options=options)

    try:
        # Open the URL and wait
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")
        driver.maximize_window()
        time.sleep(5)

        # Add a new row
        add_button = driver.find_element(By.XPATH, "//*[contains(text(),'Add')]")
        time.sleep(3)
        add_button.click()

        # Verify "Row added successfully" message
        confirmation_message = driver.find_element(By.ID, "confirmation").text
        if confirmation_message != "Row added successfully":
            sys.exit(1)

        # Enter "burger" into the new row
        new_row_input = driver.find_element(By.XPATH, "//*[@id='row2']/input")
        time.sleep(3)
        new_row_input.send_keys("burger")

        # Save the new row
        save_button = driver.find_element(By.XPATH, "//*[@id='save_btn']")
        time.sleep(3)
        save_button.click()

        # Verify "Row added successfully" message after saving
        confirmation_message = driver.find_element(By.ID, "confirmation").text
        if confirmation_message != "Row added successfully":
            sys.exit(1)

        # Remove the newly added row
        remove_button = driver.find_element(By.XPATH, "//*[@id='remove_btn']")
        time.sleep(3)
        remove_button.click()

        # Verify "Row removed successfully" message
        removal_message = driver.find_element(By.XPATH, "//div[contains(text(),'Row 2 was removed')]").text
        if removal_message != "Row 2 was removed successfully":
            sys.exit(1)

        # Exit successfully
        sys.exit(0)

    except Exception as e:
        print(str(e))
        sys.exit(1)

    finally:
        # Quit the driver
        driver.quit()

if __name__ == '__main__':
    run_test()
