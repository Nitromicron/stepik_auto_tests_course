import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)
name = browser.find_element(By.NAME, "firstname")
name.send_keys("Eduard")
lastname = browser.find_element(By.NAME, "lastname")
lastname.send_keys("Asanov")
email = browser.find_element(By.NAME, "email")
email.send_keys("edik@mail.ru")
current_dir = os.path.abspath(os.path.dirname(__file__))
file_name = 'file.txt'
file_path = os.path.join(current_dir, file_name)
element = browser.find_element(By.ID,'file')
element.send_keys(file_path)
button = browser.find_element(By.CLASS_NAME, 'btn.btn-primary').click()

time.sleep(10)
browser.quit()
