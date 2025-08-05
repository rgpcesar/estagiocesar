from selenium.webdriver.common.by import By

def test_interact_with_check_box(driver):
    driver.get("https://demoqa.com/")

    elements = driver.find_element(By.XPATH, "//*[text()='Elements']")
    elements.click()

    check_box = driver.find_element(By.ID, "item-1")
    assert check_box.is_displayed()
    check_box.click()
    
    # Clica no botão para expandir toda a árvore
    expand_all_button = driver.find_element(By.CSS_SELECTOR, "button[title='Expand all']")
    expand_all_button.click()

    # Seleciona a checkbox "Notes"
    notes_checkbox = driver.find_element(By.XPATH, "//label[@for='tree-node-notes']")
    notes_checkbox.click()
    
    # Valida se a checkbox foi marcada
    notes_input = driver.find_element(By.ID, "tree-node-notes")
    assert notes_input.is_selected()