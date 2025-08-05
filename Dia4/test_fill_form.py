import time
from selenium.webdriver.common.by import By

def test_fill_form_and_validate_output(driver):

    # driver.get("https://demoqa.com/text-box")
    driver.get("https://demoqa.com/elements")

    text_box = driver.find_element(By.ID, "item-0")
    assert text_box.is_displayed()
    text_box.click()

    # # Mapeia os elementos do formulário
    full_name_input = driver.find_element(By.ID, "userName")
    email_input = driver.find_element(By.ID, "userEmail")
    current_address_input = driver.find_element(By.ID, "currentAddress")
    permanent_address_input = driver.find_element(By.ID, "permanentAddress")
    submit_button = driver.find_element(By.ID, "submit")

    # # Dados que vamos inserir
    full_name = "Rodrigo"
    email = "rgpe@cesar.org.br"
    current_address = "Rua Barão de Souza Leão, s/n"
    permanent_address = "Avenida Boa Viagem, s/n"

    # # Preenche o formulário
    full_name_input.send_keys(full_name)
    email_input.send_keys(email)
    current_address_input.send_keys(current_address)
    permanent_address_input.send_keys(permanent_address)
    time.sleep(2)
    permanent_address_input.clear()
    time.sleep(3)
    permanent_address = "Avenida Conselheiro Aguiar, s/n"
    permanent_address_input.send_keys(permanent_address)

    
    
    # # Clica no botão de submit
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
    submit_button.click()

    time.sleep(5)
    
    # # Valida a saída
    output_name = driver.find_element(By.ID, "name")
    output_email = driver.find_element(By.ID, "email")
    output_current_address = driver.find_element(By.CSS_SELECTOR, "p#currentAddress")
    output_permanent_address = driver.find_element(By.CSS_SELECTOR, "p#permanentAddress")


    assert full_name in output_name.text
    assert email in output_email.text
    assert current_address in output_current_address.text
    assert permanent_address in output_permanent_address.text