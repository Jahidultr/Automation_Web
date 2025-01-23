import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()  # Ensure chromedriver is in PATH
    driver.maximize_window()
    yield driver
    driver.quit()


if __name__ == "__main__":
    pytest.main()