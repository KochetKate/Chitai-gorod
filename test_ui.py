import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.search_page import SearchPage

@pytest.fixture
def driver():
    """Фикстура для инициализации драйвера"""
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
    )
    driver.maximize_window()
    driver.get("https://www.chitai-gorod.ru/")
    yield driver
    driver.quit()


def test_search_by_title(driver):
    search = SearchPage(driver)
    search.search_by_title("Python")