from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x = int(browser.find_element(By.ID,"num1").text)
    y = int(browser.find_element(By.ID, "num2").text)
    result = x+y
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(result))
    button = browser.find_element(By.CLASS_NAME,"btn.btn-default")
    button.click()
finally:
    time.sleep(10)
    browser.quit()


