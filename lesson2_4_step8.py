from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

def calc(xx):
    return str(math.log(abs(12*math.sin(int(xx)))))


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

dollars = WebDriverWait(browser,12).until(
    EC.text_to_be_present_in_element((By.ID, 'price'),'$100')
)
button = browser.find_element(By.ID,'book')
button.click()
x = browser.find_element(By.ID,'input_value').text
result = calc(x)
input1 = browser.find_element   (By.CLASS_NAME, "form-control")
input1.send_keys(result)
button2 = browser.find_element(By.ID, "solve").click()

time.sleep(10)
browser.quit()