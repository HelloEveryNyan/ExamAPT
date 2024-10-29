import logging
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logger import setup_logging

setup_logging()
logger = logging.getLogger(__name__)

class UIClient:
    def __init__(self):
        with open("config.yaml") as f:
            self.data = yaml.safe_load(f)
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get(self.data["address"])
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "mdc-text-field__input")))
        username_field = self.driver.find_element(By.CLASS_NAME, "mdc-text-field__input")
        username_field.send_keys(self.data["username"])
        password_fields = self.driver.find_elements(By.CLASS_NAME, "mdc-text-field__input")
        if len(password_fields) > 1:
            password_fields[1].send_keys(self.data["password"])
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.mdc-button"))).click()

    def create_post(self, post_data):
        pass

    def close(self):
        self.driver.quit()
