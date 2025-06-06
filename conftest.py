from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
import os
import json


@pytest.fixture
def driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.hookimpl(tryfirst=True)
def pytest_sessionstart(session):
    executor_info = {
        "name": "GitHub Actions",
        "type": "github",
        "url": "https://github.com/vidd4/demoblazeTesting/actions",
        "buildOrder": "1",
        "buildName": "Test Run",
        "buildUrl": "",
        "reportUrl": ""
    }
    os.makedirs("allure-results", exist_ok=True)
    with open("allure-results/executor.json", "w") as f:
        json.dump(executor_info, f)