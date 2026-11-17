from helpers.date_helper import get_date_in
from locators.main_page_locators import MainPageLocators

ORDER_TEST_DATA = [
    {
        "button_locator": MainPageLocators.ORDER_BUTTON_TOP,
        "name": "Иван",
        "surname": "Иванов",
        "address": "Москва, ул. Пушкина, д. 10",
        "metro": "Чистые пруды",
        "phone": "+79991112233",
        "date": get_date_in(3),
        "duration": "сутки",
        "color": "black",
        "comment": "Позвонить за час до доставки",
    },
    {
        "button_locator": MainPageLocators.ORDER_BUTTON_BOTTOM,
        "name": "Анна",
        "surname": "Петрова",
        "address": "Москва, ул. Ленина, д. 5, кв. 42",
        "metro": "Арбатская",
        "phone": "+79994445566",
        "date": get_date_in(7),
        "duration": "двое суток",
        "color": "grey",
        "comment": "Оставить у консьержа",
    },
]

ORDER_IDS = ["Верхняя кнопка", "Нижняя кнопка"]