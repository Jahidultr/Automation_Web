from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


service = Service(r"C:\Windows\chromedriver.exe")

driver = webdriver.Chrome(service=service)

try:
 
    driver.get("https://www.pickaboo.com/")
    driver.maximize_window()

  
    time.sleep(5)

    
    search_box = driver.find_element(By.CLASS_NAME, "searchInput")
    search_box.send_keys("smartphone")
    search_box.send_keys(Keys.RETURN)

   
    time.sleep(5)
    products = driver.find_elements(By.CLASS_NAME, "product-item-link")
    for product in products:
        print(product.text)
finally:
 
    driver.quit()
