from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from .base_page import BasePage
import time

class DeleteQuestionPage(BasePage):
    def delete_question(self):
        self.find(By.XPATH, "//input[@name='questionIds'][@type='checkbox']").click()
        self.find(By.LINK_TEXT, "Delete").click()
        self.driver.switch_to.alert.accept()
        self.driver.switch_to.default_content()
        

        
