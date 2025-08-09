# MODO ERRADO - NÃO FAÇA ISSO!
import time
# ...
actions.double_click(double_click_btn).perform()
time.sleep(1) # Espera "cega" pela mensagem
double_click_message = driver.find_element(By.ID, "doubleClickMessage")
assert "You have done a double click" in double_click_message.text

# MODO CORRETO
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# ...
wait = WebDriverWait(driver, 10) # Espera por no máximo 10 segundos
actions.double_click(double_click_btn).perform()
# Espera ATÉ que o elemento com o ID 'doubleClickMessage' esteja visível
double_click_message = wait.until(
    EC.visibility_of_element_located((By.ID, "doubleClickMessage"))
)
assert "You have done a double click" in double_click_message.text