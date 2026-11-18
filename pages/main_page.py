from selenium.common.exceptions import TimeoutException

from data.config import BASE_URL
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    """Page Object для главной страницы Самоката"""

    def open(self):
        """Открыть главную страницу и закрыть баннер куки"""
        self.open_url(BASE_URL)
        self.close_cookie_banner()
        return self

    def close_cookie_banner(self):
        """Закрывает баннер cookie, если он появляется"""
        try:
            self.js_click(MainPageLocators.COOKIE_ACCEPT_BUTTON)
        except TimeoutException:
            pass

    def click_order_button(self, locator):
        """Нажать на кнопку 'Заказать'"""
        self.js_click(locator)

    def click_faq_question(self, question_index):
        """Нажать на вопрос в FAQ по его индексу (с 0)"""
        locator = self.format_locator(MainPageLocators.FAQ_QUESTION_TEMPLATE, question_index + 1)
        self.js_click(locator)

    def is_answer_visible(self, question_index):
        """Проверить, что ответ на вопрос стал видимым"""
        locator = self.format_locator(MainPageLocators.FAQ_ANSWER_TEMPLATE, question_index + 1)
        return self.is_element_visible(locator)

    def get_faq_answer_text(self, question_index):
        """Возвращает текст ответа на вопрос по его индексу"""
        locator = self.format_locator(MainPageLocators.FAQ_ANSWER_TEMPLATE, question_index + 1)
        return self.get_text(locator)

    def is_main_page_opened(self):
        """Проверяет, что открыта главная страница Самоката"""
        return self.is_url_to_be(BASE_URL)