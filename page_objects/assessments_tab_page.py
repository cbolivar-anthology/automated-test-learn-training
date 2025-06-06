from selenium.webdriver.common.by import By
from .base_page import BasePage

class AssessmentTabPage(BasePage):
    def create_test_button(self):
        self.find(By.LINK_TEXT, "Assessments").click()
        self.find(By.LINK_TEXT, "Test").click()
        self.find(By.LINK_TEXT, "Create").click()

