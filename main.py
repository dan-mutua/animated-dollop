from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_page_load_strategy_normal():
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'normal'
    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://www.amazon.com")
        
        # Wait for the page to load
        time.sleep(3)
        
        # Locate the search bar using its name attribute value
        search_box = driver.find_element(By.ID, "twotabsearchtextbox")
        
        # Enter "smart TVs" in the search bar and press Enter
        search_box.send_keys("smart TVs")
        search_box.send_keys(Keys.RETURN)
        
        # Wait for the search results to load
        time.sleep(3)
    finally:
        driver.quit()

def test_page_load_strategy_eager():
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'eager'
    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://www.amazon.com")
        
        # Wait for the page to load
        time.sleep(3)
        
        # Locate the search bar using its name attribute value
        search_box = driver.find_element(By.ID, "twotabsearchtextbox")
        
        # Enter "smart TVs" in the search bar and press Enter
        search_box.send_keys("smart TVs")
        search_box.send_keys(Keys.RETURN)
        
        # Wait for the search results to load
        time.sleep(3)
    finally:
        driver.quit()

if __name__ == "__main__":
    test_page_load_strategy_normal()
    test_page_load_strategy_eager()
