import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

list_of_subpages = ['236895', '236896', '236897', #subpage numbers of Stepik lessons
                    '236898', '236899', '236903',
                    '236904', '236905']

def get_time_fun():
    return math.log(int(time.time()))

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test...")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('page_num',list_of_subpages)
def test_solving_task(browser,page_num):
    link = "https://stepik.org/lesson/{}/step/1".format(page_num)
    browser.get(link)
    anser_filed = browser.find_element(By.CSS_SELECTOR,'.textarea')  # find answer area
    anser_filed.send_keys(str(get_time_fun()))  # write the answer
    submit_btn = browser.find_element(By.CSS_SELECTOR,'.submit-submission')  # find submit button
    submit_btn.click()
    authorisation = browser.find_element(By.ID, "ember521").click()
    email = browser.find_element(By.ID, "id_login_email")
    email.send_keys("edik.asanov.21@mail.ru")
    password = browser.find_element(By.ID,"id_login_password")
    password.send_keys("Pioner_1975")
    hint_message = browser.find_element(By.CSS_SELECTOR,'.smart-hints__hint')  # find message of optional feedback
    assert hint_message.text == 'Correct!', 'Fail in test on page {}'.format(link)  # compare with expexted answer
