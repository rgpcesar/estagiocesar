from selenium.webdriver.common.by import By

def test_interact_with_radio_button(driver):

    driver.get("https://demoqa.com/radio-button")
    
    # Radio buttons podem estar desabilitados ou escondidos, o que exige um click via JavaScript
    # ou, como neste caso, clicando no label associado, que é a prática recomendada.
    impressive_radio_label = driver.find_element(By.XPATH, "//label[@for='impressiveRadio']")
    impressive_radio_label.click()
    
    # Valida a mensagem
    success_message = driver.find_element(By.CSS_SELECTOR, ".mt-3")
    assert "Impressive" in success_message.text