from selenium.webdriver.common.by import By


class OrderPageLocators:
    """Локаторы страницы оформления заказа"""

    # --- Первая форма (Для кого самокат) ---
    NAME_INPUT = (By.XPATH, '//input[@placeholder="* Имя"]')
    SURNAME_INPUT = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    ADDRESS_INPUT = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    METRO_INPUT = (By.XPATH, '//input[@placeholder="* Станция метро"]')
    PHONE_INPUT = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')
    NEXT_BUTTON = (By.XPATH, '//button[text()="Далее"]')
    RENT_HEADER = (By.XPATH, '//div[text()="Про аренду"]')

    # Шаблон: вместо {} подставляется название станции (первое совпадение, есть дубли)
    METRO_OPTION_TEMPLATE = (
        By.XPATH,
        "(//button[contains(@class, 'select-search__option')]"
        "[.//div[normalize-space(text())='{}']])[1]"
    )

    # --- Вторая форма (Про аренду) ---
    DATE_INPUT = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')
    DURATION_DROPDOWN = (By.XPATH, '//div[contains(@class, "Dropdown-placeholder")]')
    # Шаблон: вместо {} подставляется срок аренды
    DURATION_OPTION_TEMPLATE = (
        By.XPATH,
        '//div[contains(@class, "Dropdown-option") and text()="{}"]'
    )
    BLACK_COLOR_CHECKBOX = (By.ID, 'black')
    GREY_COLOR_CHECKBOX = (By.ID, 'grey')
    COMMENT_INPUT = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]')
    ORDER_BUTTON = (By.XPATH, '//button[contains(@class, "Button_Middle") and text()="Заказать"]')

    # --- Модальные окна ---
    MODAL_YES_BUTTON = (By.XPATH, '//div[contains(@class, "Order_Buttons")]//button[text()="Да"]')
    SUCCESS_MESSAGE = (
        By.XPATH,
        '//div[contains(@class, "Order_ModalHeader") and contains(text(), "Заказ оформлен")]'
    )