import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class PracticeFormPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/automation-practice-form"
        # Locators
        self.FIRST_NAME_INPUT = (By.ID, "firstName")
        self.LAST_NAME_INPUT = (By.ID, "lastName")
        self.EMAIL_INPUT = (By.ID, "userEmail")
        self.GENDER_MALE_RADIO = (By.XPATH, "//label[@for='gender-radio-1']")
        self.MOBILE_INPUT = (By.ID, "userNumber")
        self.SUBMIT_BUTTON = (By.ID, "submit")
        self.CONFIRMATION_HEADER = (By.ID, "example-modal-sizes-title-lg")

    @allure.step("Navegando para a página de formulário de prática")
    def navigate(self):
        self.driver.get(self.url)

    @allure.step("Preenchendo nome e sobrenome: {first_name} {last_name}")
    def fill_name_section(self, first_name, last_name):
        self.driver.find_element(*self.FIRST_NAME_INPUT).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME_INPUT).send_keys(last_name)

    @allure.step("Preenchendo email: {email}")
    def fill_email(self, email):
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

    @allure.step("Selecionando o gênero masculino")
    def select_gender_male(self):
        self.driver.find_element(*self.GENDER_MALE_RADIO).click()
        
    @allure.step("Preenchendo o número de celular: {mobile}")
    def fill_mobile(self, mobile):
        self.driver.find_element(*self.MOBILE_INPUT).send_keys(mobile)

    @allure.step("Submetendo o formulário")
    def submit(self):
        submit_btn = self.driver.find_element(*self.SUBMIT_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
        submit_btn.click()

    @allure.step("Obtendo o texto do cabeçalho de confirmação")
    def get_confirmation_text(self):
        try:
            return self.driver.find_element(*self.CONFIRMATION_HEADER).text
        except:
            return ""