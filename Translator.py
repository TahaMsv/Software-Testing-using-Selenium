from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time


def delay():
    time.sleep(1) 

def click_element(xpath):
    element =driver.find_element(By.XPATH, xpath)
    element.click()
    delay()

def input(input_text, xpath):
    element =driver.find_element(xpath)
    element.click()
    element.clear()
    element.send_keys(input_text)
    delay()


driver = webdriver.Chrome()  
driver.get('https://targoman.ir/')  

# Select first language drop down
click_element("/html/body/div[2]/div[1]/div[1]/div[1]/div[1]")

# Select Persian
click_element("/html/body/div[2]/div[1]/div[1]/div[1]/div[1]/div/ul/li[2]")

# Select type dropdown
click_element("/html/body/div[2]/div[1]/div[1]/div[1]/div[2]/span[1]")

# Select conversational
click_element("/html/body/div[2]/div[1]/div[1]/div[1]/div[2]/div/ul/li[3]")

sentence_input =driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[1]/div[2]")
sentence_input.click()
sentence_input.clear()
sentence_input.send_keys('سلام. خوبی؟')
delay()

# Select second language drop down
click_element("/html/body/div[2]/div[1]/div[3]/div[1]/div[1]/span[1]")

# Select Germany
click_element("/html/body/div[2]/div[1]/div[3]/div[1]/div[1]/div/ul/li[3]")

# Select second language drop down
click_element("/html/body/div[2]/div[1]/div[3]/div[1]/div[1]/span[1]")

# Select English
click_element("/html/body/div[2]/div[1]/div[3]/div[1]/div[1]/div/ul/li[2]")

# Click translate
click_element("/html/body/div[2]/div[1]/div[3]/div[1]/div[3]")


# Click edit option
click_element("/html/body/div[2]/div[1]/div[3]/div[3]/ul/li[4]/a/img")

#Edite answer
sentence_input =driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[3]/div[2]")
sentence_input.click()
sentence_input.clear()
delay()
sentence_input.send_keys("Hello. Are you okey?")
delay()

#Accept changes
click_element("/html/body/div[2]/div[1]/div[3]/div[3]/ul/li[5]")

time.sleep(5)  
driver.quit()