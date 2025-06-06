from selenium.webdriver.common.by import By
from .base_page import BasePage

class QuestionTabPage(BasePage):
    def create_question_button(self, question_type):
        self.find(By.LINK_TEXT, "Create Question").click()
        self.find(By.LINK_TEXT, question_type).click()

