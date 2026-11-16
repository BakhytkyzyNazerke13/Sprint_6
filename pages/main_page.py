from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class MainPage:
    """Page Object для главной страницы Самоката"""

    URL = "https://qa-scooter.praktikum-services.ru/"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    # --- ЛОКАТОРЫ ---
    ORDER_BUTTON_TOP = (
        By.XPATH,
        "//button[contains(text(), 'Заказать') and not(contains(@class, 'Button_Middle'))]"
    )
    ORDER_BUTTON_BOTTOM = (
        By.XPATH,
        "//button[contains(text(), 'Заказать') and contains(@class, 'Button_Middle')]"
    )

    YANDEX_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoYandex')]")
    SCOOTER_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoScooter')]")

    COOKIE_ACCEPT_BUTTON = (By.ID, "rcc-confirm-button")

    # --- МЕТОДЫ ---

    def open(self):
        """Открыть главную страницу и закрыть баннер куки"""
        self.driver.get(self.URL)
        self.close_cookie_banner()
        return self

    def close_cookie_banner(self):
        """Закрывает баннер cookie, если он появляется"""
        try:
            cookie_btn = self.wait.until(EC.element_to_be_clickable(self.COOKIE_ACCEPT_BUTTON))
            self.driver.execute_script("arguments[0].click();", cookie_btn)
        except Exception:
            pass

    def _js_click(self, locator):
        """Универсальный метод для надежного клика через JavaScript"""
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.driver.execute_script("arguments[0].click();", element)

    def click_order_button(self, locator):
        """Нажать на кнопку 'Заказать'"""
        self._js_click(locator)

    def click_faq_question(self, question_index):
        """Нажать на вопрос в FAQ по его индексу"""
        dynamic_locator = (
            By.XPATH,
            f"(//div[@data-accordion-component='AccordionItemButton'])[ {question_index + 1} ]"
        )
        self._js_click(dynamic_locator)

    def is_answer_visible(self, question_index):
        """Проверить, что ответ на вопрос стал видимым"""
        dynamic_locator = (
            By.XPATH,
            f"(//div[@data-accordion-component='AccordionItemPanel'])[ {question_index + 1} ]"
        )
        try:
            self.wait.until(EC.visibility_of_element_located(dynamic_locator))
            return True
        except Exception:
            return False

    def get_faq_answer_text(self, question_index):
        """Возвращает текст ответа на вопрос по его индексу"""
        dynamic_locator = (
            By.XPATH,
            f"(//div[@data-accordion-component='AccordionItemPanel'])[ {question_index + 1} ]"
        )
        # Ждем, пока элемент станет видимым, и возвращаем его текст
        element = self.wait.until(EC.visibility_of_element_located(dynamic_locator))
        return element.text

    def click_yandex_logo(self):
        """Нажать на логотип Яндекса"""
        self._js_click(self.YANDEX_LOGO)

    def click_scooter_logo(self):
        """Нажать на логотип Самоката"""
        self._js_click(self.SCOOTER_LOGO)

    def is_main_page_opened(self):
        """Проверяет, что открыта главная страница Самоката"""
        try:
            self.wait.until(EC.url_to_be(self.URL))
            return True
        except Exception:
            return False

    def switch_to_new_window(self):
        """Ждёт появления второго окна и переключается на него"""
        self.wait.until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def is_url_contains(self, text):
        """Ждёт, пока URL текущего окна будет содержать text (с учётом редиректа)"""
        try:
            self.wait.until(EC.url_contains(text))
            return True
        except Exception:
            return False