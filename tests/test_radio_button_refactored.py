from selenium.webdriver.common.by import By
from pages.radio_button_page import RadioButtonPage
import pytest

@pytest.mark.buttons
def test_interact_with_radio_button(driver):
    radio_button_page = RadioButtonPage(driver)
    radio_button_page.navigate()

    radio_button_page.select_radio("Impressive")
    success_message =radio_button_page.get_selected_text()
    assert "Impressive" in success_message

@pytest.mark.buttons
def test_interact_with_yes_radio_button(driver):
    radio_button_page = RadioButtonPage(driver)
    radio_button_page.navigate()

    radio_button_page.select_radio("Yes")
    success_message =radio_button_page.get_selected_text()
    assert "Yes" in success_message