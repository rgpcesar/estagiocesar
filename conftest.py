import pytest
from selenium import webdriver
import time
import json
import pytest_html

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



@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Executa todos os outros hooks para obter o objeto de relatório
    outcome = yield
    report = outcome.get_result()

    # Anexa informações extras ao relatório
    extra = getattr(report, "extra", [])
    if report.when == "call":
        # Pega a fixture 'driver' do item de teste, se disponível
        driver = item.funcargs.get('driver')
        if driver is not None and report.failed:
            # Captura a screenshot e a codifica em base64
            screenshot = driver.get_screenshot_as_base64()
            # Adiciona a screenshot ao relatório HTML
            extra.append(pytest_html.extras.image(screenshot, 'Screenshot'))
        report.extra = extra