import allure
from pages.main_page import MainPage


@allure.feature("Логотипы в шапке")
class TestLogo:
    """Тесты логотипов «Самоката» и «Яндекса»"""

    @allure.title("Клик по логотипу Самоката ведёт на главную страницу")
    def test_scooter_logo_leads_to_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.open()

        # Уходим на страницу заказа, чтобы проверить возврат на главную
        main_page.click_order_button(MainPage.ORDER_BUTTON_TOP)
        main_page.click_scooter_logo()

        assert main_page.is_main_page_opened(), "Главная страница Самоката не открылась"

    @allure.title("Клик по логотипу Яндекса открывает Дзен в новом окне")
    def test_yandex_logo_opens_dzen(self, driver):
        main_page = MainPage(driver)
        main_page.open()

        main_page.click_yandex_logo()
        main_page.switch_to_new_window()

        assert main_page.is_url_contains("dzen.ru"), "Главная страница Дзена не открылась"