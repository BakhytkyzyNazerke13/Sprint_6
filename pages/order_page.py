from selenium.webdriver.common.keys import Keys

from data.config import ORDER_URL
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    """Page Object для страницы оформления заказа"""

    def wait_until_opened(self):
        """Ждёт, пока откроется страница заказа"""
        self.wait_url_to_be(ORDER_URL)

    def _select_metro(self, metro):
        """Вводит станцию и выбирает её в списке обычным кликом"""
        self.click(OrderPageLocators.METRO_INPUT)
        self.send_keys(OrderPageLocators.METRO_INPUT, metro)
        option_locator = self.format_locator(OrderPageLocators.METRO_OPTION_TEMPLATE, metro)
        self.click(option_locator)

    def fill_first_part(self, name, surname, address, metro, phone):
        """Заполняет первую часть формы"""
        self.send_keys(OrderPageLocators.NAME_INPUT, name)
        self.send_keys(OrderPageLocators.SURNAME_INPUT, surname)
        self.send_keys(OrderPageLocators.ADDRESS_INPUT, address)
        self._select_metro(metro)
        self.send_keys(OrderPageLocators.PHONE_INPUT, phone)

    def click_next(self):
        """Нажимает 'Далее' и ждёт заголовок 'Про аренду'"""
        self.js_click(OrderPageLocators.NEXT_BUTTON)
        self.find_visible(OrderPageLocators.RENT_HEADER)

    def fill_second_part(self, date, duration):
        """Заполняет вторую часть формы"""
        self.click(OrderPageLocators.DATE_INPUT)
        self.send_keys(OrderPageLocators.DATE_INPUT, date)
        self.send_keys(OrderPageLocators.DATE_INPUT, Keys.ENTER)  # подтверждаем дату

        self.click(OrderPageLocators.DURATION_DROPDOWN)
        option_locator = self.format_locator(OrderPageLocators.DURATION_OPTION_TEMPLATE, duration)
        self.click(option_locator)

    def select_color(self, color_id):
        """Выбирает цвет самоката (необязательное поле)"""
        if color_id == 'black':
            self.js_click(OrderPageLocators.BLACK_COLOR_CHECKBOX)
        elif color_id == 'grey':
            self.js_click(OrderPageLocators.GREY_COLOR_CHECKBOX)

    def fill_comment(self, comment):
        """Заполняет комментарий (необязательное поле)"""
        if comment:
            self.send_keys(OrderPageLocators.COMMENT_INPUT, comment)

    def click_order_button(self):
        """Нажимает финальную кнопку 'Заказать'"""
        self.js_click(OrderPageLocators.ORDER_BUTTON)

    def click_modal_yes(self):
        """Нажимает 'Да' в окне 'Хотите оформить заказ?'"""
        self.js_click(OrderPageLocators.MODAL_YES_BUTTON)

    def is_success_message_visible(self):
        """Проверяет окно 'Заказ оформлен'"""
        return self.is_element_visible(OrderPageLocators.SUCCESS_MESSAGE)