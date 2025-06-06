from selenium.webdriver.common.by import By
from .base_page import BasePage
import time

class CreateQuestionPage(BasePage):
    def create_boolean_question(self, question_title, question_text):
        self.find(By.ID, "questionTitle").send_keys(question_title)
        time.sleep(3)
        iframe = self.find(By.ID, "questionText.text_ifr")
        self.driver.switch_to.frame(iframe)
        self.find(By.TAG_NAME, "p").send_keys(question_text)
        self.driver.switch_to.default_content()
        self.find(By.XPATH, "//p[@id='bottom_submitButtonRow']/input[3]").click()

