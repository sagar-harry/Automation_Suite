
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_blog_page():
    try:
        # Set up Chrome options for headless mode, incognito, and other configurations
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--disable-features=NetworkService")

        # Initialize the WebDriver
        driver = webdriver.Chrome(options=chrome_options)

        # Maximize the window
        driver.maximize_window()

        # Navigate to the homepage
        driver.get("https://practicetestautomation.com")
        
        # Wait 5 seconds after page load
        time.sleep(5)

        # Wait for "Blog" menu element and click
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Blog')]"))
        )
        time.sleep(3)
        blog_menu = driver.find_element(By.XPATH, "//a[contains(text(),'Blog')]")
        blog_menu.click()

        # Wait for page to load
        time.sleep(3)
        current_url = driver.current_url

        # Verify the page URL
        if current_url == "https://practicetestautomation.com/blog/":
            driver.quit()
            exit(0)
        else:
            driver.quit()
            exit(1)

    except Exception as e:
        driver.quit()
        exit(1)

if __name__ == "__main__":
    test_blog_page()
