from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class OrderPage:
    """Page Object для страницы оформления заказа"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    # --- ЛОКАТОРЫ: первая форма (Для кого самокат) ---
    NAME_INPUT = (By.XPATH, '//input[@placeholder="* Имя"]')
    SURNAME_INPUT = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    ADDRESS_INPUT = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    METRO_INPUT = (By.XPATH, '//input[@placeholder="* Станция метро"]')
    PHONE_INPUT = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')
    NEXT_BUTTON = (By.XPATH, '//button[text()="Далее"]')
    RENT_HEADER = (By.XPATH, '//div[text()="Про аренду"]')

    # --- ЛОКАТОРЫ: вторая форма (Про аренду) ---
    DATE_INPUT = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')
    DURATION_DROPDOWN = (By.XPATH, '//div[contains(@class, "Dropdown-placeholder")]')
    BLACK_COLOR_CHECKBOX = (By.ID, 'black')
    GREY_COLOR_CHECKBOX = (By.ID, 'grey')
    COMMENT_INPUT = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]')
    ORDER_BUTTON = (By.XPATH, '//button[contains(@class, "Button_Middle") and text()="Заказать"]')

    # --- ЛОКАТОРЫ: модальные окна ---
    MODAL_YES_BUTTON = (By.XPATH, '//div[contains(@class, "Order_Buttons")]//button[text()="Да"]')
    SUCCESS_MESSAGE = (
        By.XPATH,
        '//div[contains(@class, "Order_ModalHeader") and contains(text(), "Заказ оформлен")]'
    )

    # --- ВСПОМОГАТЕЛЬНЫЕ МЕТОДЫ ---

    def _js_click(self, locator):
        """Клик через JavaScript (для обычных кнопок и чекбоксов)"""
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.driver.execute_script("arguments[0].click();", element)

    def _select_metro(self, metro):
        """Вводит станцию и выбирает её в списке обычным кликом"""
        metro_field = self.wait.until(EC.element_to_be_clickable(self.METRO_INPUT))
        metro_field.click()
        metro_field.send_keys(metro)

        option_locator = (
            By.XPATH,
            f"(//button[contains(@class, 'select-search__option')]"
            f"[.//div[normalize-space(text())='{metro}']])[1]"
        )
        option = self.wait.until(EC.element_to_be_clickable(option_locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", option)
        option.click()

    # --- МЕТОДЫ СТРАНИЦЫ ---

    def fill_first_part(self, name, surname, address, metro, phone):
        """Заполняет первую часть формы"""
        self.wait.until(EC.visibility_of_element_located(self.NAME_INPUT)).send_keys(name)
        self.driver.find_element(*self.SURNAME_INPUT).send_keys(surname)
        self.driver.find_element(*self.ADDRESS_INPUT).send_keys(address)
        self._select_metro(metro)
        self.driver.find_element(*self.PHONE_INPUT).send_keys(phone)

    def click_next(self):
        """Нажимает 'Далее' и ждёт заголовок 'Про аренду'"""
        self._js_click(self.NEXT_BUTTON)
        self.wait.until(EC.visibility_of_element_located(self.RENT_HEADER))

    def fill_second_part(self, date, duration):
        """Заполняет вторую часть формы"""
        date_input = self.wait.until(EC.visibility_of_element_located(self.DATE_INPUT))
        date_input.click()
        date_input.send_keys(date)
        date_input.send_keys(Keys.ENTER)  # подтверждаем дату и закрываем календарь

        self.wait.until(EC.element_to_be_clickable(self.DURATION_DROPDOWN)).click()
        option_locator = (
            By.XPATH,
            f'//div[contains(@class, "Dropdown-option") and text()="{duration}"]'
        )
        self.wait.until(EC.element_to_be_clickable(option_locator)).click()

    def select_color(self, color_id):
        """Выбирает цвет самоката (необязательное поле)"""
        if color_id == 'black':
            self._js_click(self.BLACK_COLOR_CHECKBOX)
        elif color_id == 'grey':
            self._js_click(self.GREY_COLOR_CHECKBOX)

    def fill_comment(self, comment):
        """Заполняет комментарий (необязательное поле)"""
        if comment:
            self.driver.find_element(*self.COMMENT_INPUT).send_keys(comment)

    def click_order_button(self):
        """Нажимает финальную кнопку 'Заказать'"""
        self._js_click(self.ORDER_BUTTON)

    def click_modal_yes(self):
        """Нажимает 'Да' в окне 'Хотите оформить заказ?'"""
        self._js_click(self.MODAL_YES_BUTTON)

    def is_success_message_visible(self):
        """Проверяет окно 'Заказ оформлен'"""
        try:
            self.wait.until(EC.visibility_of_element_located(self.SUCCESS_MESSAGE))
            return True
        except Exception:
            return False