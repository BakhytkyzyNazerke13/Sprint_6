import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def driver():
    browser = webdriver.Firefox()
    
    browser.maximize_window() # Разворачиваем браузер на весь экран
    
    yield browser # Передаем управление тесту
    
    browser.quit() # Закрываем браузер после теста