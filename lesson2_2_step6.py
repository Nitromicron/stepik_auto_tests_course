from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(xx):
    return str(math.log(abs(12*math.sin(int(xx)))))
try:
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element(By.ID,'input_value').text
    result = calc(x)
    input1 = browser.find_element(By.CLASS_NAME,"form-control")
    input1.send_keys(result)
    button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    checkbox = browser.find_element(By.ID,"robotCheckbox").click()
    radiobox = browser.find_element(By.ID,"robotsRule").click()
    button.click()
finally:
    time.sleep(10)
    browser.quit()

