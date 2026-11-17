import allure
import pytest

from data.order_data import ORDER_IDS, ORDER_TEST_DATA
from pages.main_page import MainPage
from pages.order_page import OrderPage


@allure.feature("Оформление заказа самоката")
class TestOrder:
    """Тесты позитивного сценария заказа самоката"""

    @allure.title("Позитивный сценарий заказа самоката")
    @pytest.mark.parametrize("data", ORDER_TEST_DATA, ids=ORDER_IDS)
    def test_positive_order_flow(self, driver, data):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_order_button(data["button_locator"])

        order_page = OrderPage(driver)
        order_page.fill_first_part(
            name=data["name"],
            surname=data["surname"],
            address=data["address"],
            metro=data["metro"],
            phone=data["phone"]
        )
        order_page.click_next()

        order_page.fill_second_part(date=data["date"], duration=data["duration"])
        order_page.select_color(data["color"])
        order_page.fill_comment(data["comment"])

        order_page.click_order_button()
        order_page.click_modal_yes()

        assert order_page.is_success_message_visible(), "Сообщение 'Заказ оформлен' не появилось!"