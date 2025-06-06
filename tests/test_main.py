import os
from selenium import webdriver
from dotenv import load_dotenv
from page_objects.login_page import LoginPage
from page_objects.assessments_tab_page import AssessmentTabPage
from page_objects.create_test_page import CreateTestPage
from page_objects.questions_tab_page import QuestionTabPage
from page_objects.create_question_page import CreateQuestionPage
from page_objects.delete_question_page import DeleteQuestionPage
from selenium.webdriver.common.by import By

import time 

load_dotenv()

def get_driver():
    browser = os.getenv("BROWSER", "chrome")

    # fallback to local driver
    if browser == "chrome":
        return webdriver.Chrome()
    elif browser == "firefox":
        return webdriver.Firefox()
    else:
        raise Exception("Unsupported browser")

def test_utlra_test_creation():
    driver = get_driver()
    url = os.getenv("INITIAL_URL")
    username = os.getenv("LEARN_USERNAME")
    password = os.getenv("LEARN_PASSWORD")
    course_content_url= os.getenv("COURSE_CONTENT_URL")

    try:
        driver.get(url)
        LoginPage(driver).login(username, password)
        driver.get(course_content_url)
        AssessmentTabPage(driver).create_test_button()
        CreateTestPage(driver).create_test("Automated Test Assessment 1")
        QuestionTabPage(driver).create_question_button("True/False")
        CreateQuestionPage(driver).create_boolean_question(question_title="Boolean Question", question_text="This is from an Automated test")
        time.sleep(5)
        assert driver.find_element(By.XPATH, "//div[@id='receipt_nested_id']/span").text == "Success: Question created."
        DeleteQuestionPage(driver).delete_question()
        assert int(driver.find_element(By.ID, "totalQuestions").text) == 0
    finally:
        driver.quit()
