from selenium.webdriver.common.by import By

class MainPageLocators:
    """Локаторы главной страницы"""

    ORDER_BUTTON_TOP = (
        By.XPATH,
        "//button[contains(text(), 'Заказать') and not(contains(@class, 'Button_Middle'))]"
    )
    ORDER_BUTTON_BOTTOM = (
        By.XPATH,
        "//button[contains(text(), 'Заказать') and contains(@class, 'Button_Middle')]"
    )
    COOKIE_ACCEPT_BUTTON = (By.ID, "rcc-confirm-button")

    # Шаблоны: вместо {} подставляется порядковый номер вопроса (с 1)
    FAQ_QUESTION_TEMPLATE = (
        By.XPATH,
        "(//div[@data-accordion-component='AccordionItemButton'])[{}]"
    )
    FAQ_ANSWER_TEMPLATE = (
        By.XPATH,
        "(//div[@data-accordion-component='AccordionItemPanel'])[{}]"
    )