from selenium.webdriver.common.by import By

def test_navigate_to_elements_page(driver):
    """Navega para a página de elementos."""
    driver.get("https://demoqa.com/elements")
    assert "elements" in driver.current_url

def test_find_text_box_button_by_id(driver):
    """Localiza o botão 'Text Box' pelo seu ID."""
    driver.get("https://demoqa.com/elements")
    # A estratégia By.ID procura por um elemento com o atributo id="item-0"
    element = driver.find_element(By.ID, "item-0")
    assert element.is_displayed()
    assert element.text == "Text Box"

def test_find_text_box_button_by_css_selector(driver):
    """Localiza o botão 'Text Box' por CSS Selector."""
    driver.get("https://demoqa.com/elements")
    # Seleciona o elemento com id 'item-0'
    element = driver.find_element(By.CSS_SELECTOR, "#item-0")
    assert element.is_displayed()

def test_find_text_box_button_by_xpath(driver):
    """Localiza o botão 'Text Box' por XPath."""
    driver.get("https://demoqa.com/elements")
    # Seleciona o elemento <li> que contém um <span> com o texto "Text Box"
    element = driver.find_element(By.XPATH, "//span[text()='Text Box']")
    assert element.is_displayed()