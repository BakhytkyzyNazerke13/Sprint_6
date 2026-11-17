import allure
import pytest

from data.faq_data import FAQ_DATA, FAQ_IDS
from pages.main_page import MainPage


@allure.feature("Раздел 'Вопросы о важном'")
class TestFaq:
    """Тесты для проверки работы аккордеона с вопросами"""

    @allure.title("Проверка открытия ответа и сверка текста в FAQ")
    @pytest.mark.parametrize("question_index, expected_text", FAQ_DATA, ids=FAQ_IDS)
    def test_faq_question_opens_and_text_matches(self, driver, question_index, expected_text):
        main_page = MainPage(driver)
        main_page.open()

        main_page.click_faq_question(question_index)
        actual_text = main_page.get_faq_answer_text(question_index)

        assert actual_text.strip() == expected_text.strip(), (
            f"Текст ответа не совпадает для вопроса {question_index + 1}!\n"
            f"Ожидалось: {expected_text}\n"
            f"Получено: {actual_text}"
        )