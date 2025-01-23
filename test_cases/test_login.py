import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.NAME, 'userEmail')
        self.password_field = (By.NAME, 'userPassword')
        self.login_button = (By.TAG_NAME, 'button')
        self.clickLogin = (By.CLASS_NAME,'input-field')
    
    def FClick(self):
        self.driver.find_element(*self.clickLogin).click()

    def enter_username(self, username):
        self.driver.find_element(*self.username_field).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

@pytest.fixture
def driver():
    driver = webdriver.Chrome() 
    driver.get("https://www.pickaboo.com/login/")
    yield driver
    driver.quit()

def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.FClick()
    time.sleep(2)
    login_page.enter_username("jahidulislamdiu02@gmail.com")
    login_page.enter_password("As@208660%%")
    time.sleep(5)
    #login_page.click_login()
     # Debugging outputs
    assert "dashboard" in driver.current_url

def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.FClick()
    time.sleep(2)
    login_page.enter_username("wrong_user@gmail.com")
    login_page.enter_password("wrong_password")
    time.sleep(5)
    #login_page.click_login()
    #error_message = driver.find_element(By.ID, "error-msg").text
    #assert "Invalid credentials" in error_message