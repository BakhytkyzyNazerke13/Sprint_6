from datetime import datetime, timedelta

import allure
import pytest

from pages.main_page import MainPage
from pages.order_page import OrderPage


def _date_in(days):
    """Возвращает дату через N дней в формате ДД.ММ.ГГГГ"""
    return (datetime.now() + timedelta(days=days)).strftime("%d.%m.%Y")


# Наборы тестовых данных для параметризации
ORDER_TEST_DATA = [
    {
        "entry_point": "Верхняя кнопка 'Заказать'",
        "button_locator": MainPage.ORDER_BUTTON_TOP,
        "name": "Иван",
        "surname": "Иванов",
        "address": "Москва, ул. Пушкина, д. 10",
        "metro": "Чистые пруды",
        "phone": "+79991112233",
        "date": _date_in(3),
        "duration": "сутки",
        "color": "black",
        "comment": "Позвонить за час до доставки"
    },
    {
        "entry_point": "Нижняя кнопка 'Заказать'",
        "button_locator": MainPage.ORDER_BUTTON_BOTTOM,
        "name": "Анна",
        "surname": "Петрова",
        "address": "Москва, ул. Ленина, д. 5, кв. 42",
        "metro": "Арбатская",
        "phone": "+79994445566",
        "date": _date_in(7),
        "duration": "двое суток",
        "color": "grey",
        "comment": "Оставить у консьержа"
    }
]


@allure.feature("Оформление заказа самоката")
class TestOrder:
    """Тесты позитивного сценария заказа самоката"""

    @allure.title("Позитивный сценарий заказа самоката")
    @pytest.mark.parametrize("data", ORDER_TEST_DATA, ids=["Верхняя кнопка", "Нижняя кнопка"])
    def test_positive_order_flow(self, driver, data):
        """
        Тест проверяет полный цикл заказа: от нажатия кнопки 'Заказать'
        до появления сообщения об успешном оформлении.
        """
        # 1. Открываем главную страницу
        main_page = MainPage(driver)
        main_page.open()

        # 2. Нажимаем на кнопку Заказать (верхнюю или нижнюю кнопку)
        main_page.click_order_button(data["button_locator"])

        # 3. Заполняем первую часть формы и жмем "Далее"
        order_page = OrderPage(driver)
        order_page.fill_first_part(
            name=data["name"],
            surname=data["surname"],
            address=data["address"],
            metro=data["metro"],
            phone=data["phone"]
        )
        order_page.click_next()

        # 4. Заполняем вторую часть формы (аренда)
        order_page.fill_second_part(
            date=data["date"],
            duration=data["duration"]
        )

        # 5. Выбираем цвет и добавляем комментарий
        order_page.select_color(data["color"])
        order_page.fill_comment(data["comment"])

        # 6. Нажимаем финальную кнопку "Заказать"
        order_page.click_order_button()

        # 7. Подтверждаем заказ в окне
        order_page.click_modal_yes()

        # 8. ПРОВЕРКА: убеждаемся, что появилось сообщение об успехе
        assert order_page.is_success_message_visible(), "Сообщение 'Заказ оформлен' не появилось!"