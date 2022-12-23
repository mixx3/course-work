import requests
import selenium.common.exceptions
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

ORIGIN_URL = "https://market.yandex.ru"


def proudly_recieve_chrome_driver() -> webdriver.Chrome:
    try:
        return webdriver.Chrome()
    except selenium.common.exceptions.WebDriverException:
        s = Service(ChromeDriverManager().install())
        return webdriver.Chrome(service=s)
