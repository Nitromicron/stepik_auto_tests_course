from locale import windows_locale

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(xx):
    return str(math.log(abs(12*math.sin(int(xx)))))
link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)
button1 = browser.find_element(By.CLASS_NAME, "trollface.btn.btn-primary").click()
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)
x = browser.find_element(By.ID,'input_value').text
result = calc(x)
input1 = browser.find_element(By.CLASS_NAME, "form-control")
input1.send_keys(result)
button2 = browser.find_element(By.CLASS_NAME, "btn.btn-primary").click()
time.sleep(10)
browser.quit()