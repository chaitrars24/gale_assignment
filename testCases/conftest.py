import pytest as pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def setup():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.ixigo.com/flights")
    driver.maximize_window()
    driver.implicitly_wait(20)
    yield driver
    driver.quit()
    return driver
