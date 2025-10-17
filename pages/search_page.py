from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class SearchPage:
    """
    Класс для выполнения поиска книг по названию на сайте Читай-город.
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы авторизации.
        :param driver: Экземпляр WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        
        # Локаторы для поисковой строки
        self.search = (By.CSS_SELECTOR, "input[name='search']")
        self.search_button = (By.CSS_SELECTOR, "button[type='submit'].search-form__button-search")


    def search_by_title(self, book_title):
        # Ввод названия в строку поиска
        search_input = self.driver.find_element(*self.search)
        search_input.send_keys(book_title)
        # Клик по кнопке поиска
        search_button = self.driver.find_element(*self.search_button)
        search_button.click()
