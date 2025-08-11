from selenium.webdriver.common.by import By

class RadioButtonPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/radio-button"
        #locators
        self.IMPRESSIVE_RADIO_LABEL = (By.XPATH, "//label[@for='impressiveRadio']")
        self.YES_RADIO_LABEL = (By.XPATH, "//label[@for='yesRadio']")
        self.SELECTED_TEXT = (By.CSS_SELECTOR, ".mt-3")

    def navigate(self):
        self.driver.get(self.url)
    
    def select_radio(self, selectOption):
        if selectOption == 'Yes':
            radio_button = self.driver.find_element(*self.YES_RADIO_LABEL)
        else:
            radio_button = self.driver.find_element(*self.IMPRESSIVE_RADIO_LABEL)
        radio_button.click()

    def get_selected_text(self):
        return self.driver.find_element(*self.SELECTED_TEXT).text


    