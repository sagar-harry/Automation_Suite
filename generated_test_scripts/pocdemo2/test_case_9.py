
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def test_add_row():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-notifications')
    options.add_argument('--incognito')
    options.add_argument('--disable-features=NetworkService')

    driver = webdriver.Chrome(options=options)

    try:
        driver.get("URL_OF_TEST_EXCEPTIONS_PAGE")  # Please replace with actual URL
        driver.maximize_window()
        time.sleep(5)  # Step 4: Wait for 5 secs after opening the page

        # Step 1: Navigate to the "Test Exceptions" page
        # Step 2: Click on the "Add" button to add a new row.
        time.sleep(3)  # Step 6: Wait for 3 secs before every action
        add_button = driver.find_element(By.XPATH, "//button[contains(text(),'Add')]")
        add_button.click()

        # Step 3: Verify the message "Row added successfully".
        time.sleep(3)  # Wait for interaction to complete
        confirmation_msg = driver.find_element(By.XPATH, "//*[@id='confirmation']").text
        if confirmation_msg != "Row added successfully":
            raise Exception("Confirmation message does not match expected message")

        # Step 4: Enter "burger" into the newly added row input field.
        time.sleep(3)  # Step 6: Wait for 3 secs before every action
        input_field = driver.find_element(By.XPATH, "//*[@id='row2']/input")
        input_field.send_keys("burger")

        # Step 5: Click on the "Save" button.
        time.sleep(3)  # Step 6: Wait for 3 secs before every action
        save_button = driver.find_element(By.XPATH, "//*[@id='save_btn']")
        save_button.click()

        # Step 6: Verify the message "Row added successfully".
        time.sleep(3)  # Wait again for the message to appear
        confirmation_msg = driver.find_element(By.XPATH, "//*[@id='confirmation']").text
        if confirmation_msg != "Row added successfully":
            raise Exception("Save confirmation message does not match expected message")

        driver.quit()
        exit(0)  # Test passed

    except Exception as e:
        print(f"Test failed: {str(e)}")
        driver.quit()
        exit(1)  # Test failed

# Run the test
test_add_row()
