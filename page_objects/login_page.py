from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    def login(self, username, password):
        self.find(By.ID, "agree_button").click()
        self.find(By.ID, "user_id").send_keys(username)
        self.find(By.ID, "password").send_keys(password)
        self.find(By.ID, "entry-login").submit()

