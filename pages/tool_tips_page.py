from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ToolTipsPage:
    #locators
    TOOL_TIP_BUTTON = (By.ID, "toolTipButton")
    TOOP_TIP_INPUT = (By.ID, "toolTipTextField")
    TOOL_TIP_MESSAGE = (By.CSS_SELECTOR, ".tooltip-inner")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def navigate(self, url):
        self.driver.get(url)

    def hover_over_button(self):
        button = self.driver.find_element(*self.TOOL_TIP_BUTTON)
        ActionChains(self.driver).move_to_element(button).perform()

    def hover_over_fied(self):
        text_input = self.driver.find_element(*self.TOOP_TIP_INPUT)
        ActionChains(self.driver).move_to_element(text_input).perform()

    def get_tooltip_text(self):
        tooltip = self.wait.until(EC.visibility_of_element_located(self.TOOL_TIP_MESSAGE))
        return tooltip.text


