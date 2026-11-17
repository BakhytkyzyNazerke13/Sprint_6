from selenium.webdriver.common.by import By

class BasePageLocators:
    """Локаторы шапки (есть на каждой странице)"""

    YANDEX_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoYandex')]")
    SCOOTER_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoScooter')]")