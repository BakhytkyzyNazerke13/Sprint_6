from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from locators.base_page_locators import BasePageLocators


class BasePage:
    """Базовый Page Object: общие методы и элементы шапки для всех страниц"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    # --- РАБОТА С БРАУЗЕРОМ ---

    def open_url(self, url):
        """Открывает страницу по адресу"""
        self.driver.get(url)

    def switch_to_new_window(self):
        """Ждёт появления второго окна и переключается на него"""
        self.wait.until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def is_url_to_be(self, url):
        """Ждёт, пока URL станет равен url"""
        try:
            self.wait.until(EC.url_to_be(url))
            return True
        except TimeoutException:
            return False

    def wait_url_to_be(self, url):
        """Ждёт, пока URL станет равен url (без возврата результата)"""
        self.wait.until(EC.url_to_be(url))

    def is_url_contains(self, text):
        """Ждёт, пока URL будет содержать text (с учётом редиректа)"""
        try:
            self.wait.until(EC.url_contains(text))
            return True
        except TimeoutException:
            return False

    # --- РАБОТА С ЭЛЕМЕНТАМИ ---

    @staticmethod
    def format_locator(locator_template, value):
        """Подставляет значение в шаблон локатора: (By, 'xpath с {}') -> (By, 'xpath со значением')"""
        by, selector = locator_template
        return by, selector.format(value)

    def find_visible(self, locator):
        """Ждёт, пока элемент станет видимым, и возвращает его"""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def scroll_to_element(self, element):
        """Прокручивает страницу до элемента"""
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def click(self, locator):
        """Обычный клик: ждёт кликабельности, прокручивает к элементу, кликает"""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self.scroll_to_element(element)
        element.click()

    def js_click(self, locator):
        """Клик через JavaScript (для кнопок, которые перекрыты другими элементами)"""
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.scroll_to_element(element)
        self.driver.execute_script("arguments[0].click();", element)

    def send_keys(self, locator, text):
        """Вводит текст в поле"""
        self.find_visible(locator).send_keys(text)

    def get_text(self, locator):
        """Возвращает текст видимого элемента"""
        return self.find_visible(locator).text

    def is_element_visible(self, locator):
        """Проверяет, что элемент стал видимым"""
        try:
            self.find_visible(locator)
            return True
        except TimeoutException:
            return False

    # --- ШАПКА ---

    def click_yandex_logo(self):
        """Нажать на логотип Яндекса"""
        self.js_click(BasePageLocators.YANDEX_LOGO)

    def click_scooter_logo(self):
        """Нажать на логотип Самоката"""
        self.js_click(BasePageLocators.SCOOTER_LOGO)