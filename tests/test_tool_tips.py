import time
from pages.tool_tips_page import ToolTipsPage
import pytest

@pytest.mark.widgets
def test_tool_tips_flow(driver, test_data):

    tool_tips_page = ToolTipsPage(driver)

    tool_tips_page.navigate(test_data['tool_tips_url'])

    tool_tips_page.hover_over_button()
    tool_tip_button = tool_tips_page.get_tooltip_text()
    assert tool_tip_button == test_data['expected_button_tooltip']

    tool_tips_page.hover_over_fied()
    time.sleep(2)
    tool_tip_input = tool_tips_page.get_tooltip_text()
    assert tool_tip_input == test_data['expected_input_tooltip']