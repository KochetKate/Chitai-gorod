from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def get_fresh_cookies() -> dict:
    """
    Получить свежие куки через Selenium.
    :return: словарь с куками
    :rtype: dict
    """
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        driver.get("https://www.chitai-gorod.ru/")
        driver.implicitly_wait(10)
        # Получаем все куки
        cookies = driver.get_cookies()
        # Фильтруем только нужные куки DDOS-Guard
        cookies_dict = {}
        for cookie in cookies:
            if cookie['name'].startswith('__ddg'):
                cookies_dict[cookie['name']] = cookie['value']

        return cookies_dict

    finally:
        driver.quit()
