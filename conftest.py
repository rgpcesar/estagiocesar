import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    """
    Fixture que inicializa e finaliza o WebDriver para cada teste.
    """
    instance = webdriver.Chrome()
    # instance = webdriver.Firefox()

    yield instance

    instance.quit()