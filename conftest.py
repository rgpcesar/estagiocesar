import pytest
from selenium import webdriver
import time
import json

# @pytest.fixture
# def driver():
#     """
#     Fixture que inicializa e finaliza o WebDriver para cada teste.
#     """
#     instance = webdriver.Chrome()
#     # instance = webdriver.Firefox()

#     yield instance

#     instance.quit()


# Esta função adiciona a opção --browser na linha de comando
def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Navegador para executar os testes: chrome ou firefox"
    )

# A fixture 'driver' agora lê a opção da linha de comando
@pytest.fixture(scope="function")
def driver(request):
    browser_name = request.config.getoption("--browser")
    
    print(f"\n[INFO] Initializing {browser_name} driver...")
    
    if browser_name.lower() == "chrome":
        instance = webdriver.Chrome()
    elif browser_name.lower() == "firefox":
        instance = webdriver.Firefox()
    else:
        raise ValueError(f"Browser '{browser_name}' is not supported.")
        
    start_time = time.time()

    yield instance

    end_time = time.time()
    duration = end_time - start_time
    
    print(f"\n[INFO] Test on {browser_name} finished in {duration:.2f} seconds.")
    instance.quit()


@pytest.fixture(scope="session")
def test_data():
    with open('data/test_data.json', 'r') as f:
        data = json.load(f)
    return data