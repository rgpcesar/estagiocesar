import pytest
import json
from pages.form_page import PracticeFormPage
import allure

def load_form_data():
    with open('data/form_data.json', 'r') as f:
        return json.load(f)

@allure.epic("Formulários")
@allure.feature("Formulário de Prática")
@pytest.mark.forms
class TestPracticeForm:

    @allure.story("Preenchimento bem-sucedido do formulário")
    @allure.title("Testar preenchimento do formulário de prática com dados válidos")
    @pytest.mark.parametrize("user_data", load_form_data())
    def test_fill_practice_form(self, driver, user_data):
        form_page = PracticeFormPage(driver)
        
        form_page.navigate()
        form_page.fill_name_section(user_data["first_name"], user_data["last_name"])
        form_page.fill_email(user_data["email"])
        form_page.select_gender_male()
        form_page.fill_mobile(user_data["mobile"])
        form_page.submit()
        
        confirmation_text = form_page.get_confirmation_text()
        assert "Thanks for submitting the form" in confirmation_text, \
            "A mensagem de confirmação não foi encontrada ou está incorreta."