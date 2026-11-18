import allure

from data.config import DZEN_DOMAIN
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
from pages.order_page import OrderPage


@allure.feature("Логотипы в шапке")
class TestLogo:
    """Тесты логотипов «Самоката» и «Яндекса»"""

    @allure.title("Клик по логотипу Самоката ведёт на главную страницу")
    def test_scooter_logo_leads_to_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.open()

        # Уходим на страницу заказа, чтобы проверить возврат на главную
        main_page.click_order_button(MainPageLocators.ORDER_BUTTON_TOP)
        order_page = OrderPage(driver)
        order_page.wait_until_opened()

        order_page.click_scooter_logo()

        assert main_page.is_main_page_opened(), "Главная страница Самоката не открылась"

    @allure.title("Клик по логотипу Яндекса открывает Дзен в новом окне")
    def test_yandex_logo_opens_dzen(self, driver):
        main_page = MainPage(driver)
        main_page.open()

        main_page.click_yandex_logo()
        main_page.switch_to_new_window()

        assert main_page.is_url_contains(DZEN_DOMAIN), "Главная страница Дзена не открылась"