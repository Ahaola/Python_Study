import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver

@pytest.fixture(scope="module") # scope表示fixture的访问权限
def driver():
    d = webdriver.Firefox()
    return d