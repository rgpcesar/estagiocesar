import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def test_button_clicks(driver):
    """
    Testa os diferentes tipos de cliques: duplo, direito e simples.
    """
    driver.get("https://demoqa.com/buttons")
    actions = ActionChains(driver)

    # # 1. Double Click
    # double_click_btn = driver.find_element(By.ID, "doubleClickBtn")
    # actions.double_click(double_click_btn).perform()
    # double_click_message = driver.find_element(By.ID, "doubleClickMessage")
    # assert "You have done a double click" in double_click_message.text
    

    # # 2. Right Click
    # right_click_btn = driver.find_element(By.ID, "rightClickBtn")
    # actions.context_click(right_click_btn).perform()
    # right_click_message = driver.find_element(By.ID, "rightClickMessage")
    # assert "You have done a right click" in right_click_message.text
    
    # 3. Dynamic Click (Simples)
    # O XPath aqui é mais complexo porque o botão não tem um ID fixo
    dynamic_click_btn = driver.find_element(By.XPATH, "//button[text()='Click Me']") 
    dynamic_click_btn.click()
    dynamic_click_message = driver.find_element(By.ID, "dynamicClickMessage")
    assert "You have done a dynamic click" in dynamic_click_message.text
    time.sleep(3)