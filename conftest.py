from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
import tempfile
import shutil


@pytest.fixture
def driver():
    options = Options()
    user_data_dir = tempfile.mkdtemp()
    options.add_argument(f'--user-data-dir={user_data_dir}')
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
    shutil.rmtree(user_data_dir)