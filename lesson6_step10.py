from selenium import webdriver
from selenium.webdriver.common.by import By
import time


try:
    link = "https://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    label1 = browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.first')
    label1.send_keys("Eduard")
    label2 = browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.second')
    label2.send_keys("Asanov")
    label3 = browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.third')
    label3.send_keys("edik@mail.ru")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

except:
    time.sleep(30)
    browser.quit()