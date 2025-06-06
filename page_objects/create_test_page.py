from selenium.webdriver.common.by import By
from .base_page import BasePage

class CreateTestPage(BasePage):
    def create_test(self, test_name):
        self.find(By.ID, "assessment_name_input").send_keys(test_name)
        self.find(By.ID, "bottom_Submit").submit()

