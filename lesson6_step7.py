import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from faker import Faker
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    fake = Faker()
    word = fake.word()
    elements = browser.find_elements(By.TAG_NAME,"input")
    for element in elements:
        element.send_keys(word)

    button_click = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button_click.click()
finally:
    time.sleep(30)
    browser.quit()



