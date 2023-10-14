from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time


def delay():
    time.sleep(1.5) 

driver = webdriver.Chrome()  
driver.get('https://www.alibaba.ir/')  

bus_trips =driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/main/div/div[2]/div[1]/div[1]/ul/li[4]")
bus_trips.click()
delay()

source_city_input =driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/main/div/div[2]/div[1]/div[2]/div/form/div/div[1]/div/div[1]/div[1]/span/input")
source_city_input.clear()
source_city_input.send_keys('تهران')
delay()
# source_city_input.send_keys(Keys.TAB)


source_city_option =driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/main/div/div[2]/div[1]/div[2]/div/form/div/div[1]/div/div[2]/div/ul/li[2]")
source_city_option.click()
delay()

destination_city_input =driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/main/div/div[2]/div[1]/div[2]/div/form/div/div[1]/div/div[1]/div[2]/span[1]/input")
destination_city_input.clear()
destination_city_input.send_keys('اصفهان')
time.sleep(3) 
# destination_city_input.send_keys(Keys.TAB)

destination_city_option =driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/main/div/div[2]/div[1]/div[2]/div/form/div/div[1]/div/div[2]/div/ul/li[1]")
destination_city_option.click()
delay()

today_date = driver.find_element(By.CLASS_NAME,  'is-today')
today_date.click()
delay()

search_btn = driver.find_element(By.XPATH,  '/html/body/div[1]/div[1]/main/div/div[2]/div[1]/div[2]/div/form/div/div[3]/button')
search_btn.click()
time.sleep(10) 

sort_by_earliest_btn = driver.find_element(By.XPATH,  '/html/body/div[1]/div[1]/main/div/div/section/div[1]/ul/li[3]/a')
sort_by_earliest_btn.click()
delay()


select_ticket_btn = driver.find_element(By.XPATH,  '/html/body/div[1]/div[1]/main/div/div/section/div[2]/div/div[2]/button')
if(select_ticket_btn):
    select_ticket_btn.click()
    delay()
    title = driver.find_element(By.XPATH,  '/html/body/div[1]/div[1]/main/form/div[1]/div/div/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div[2]/strong')
    print(title.text)

    time = driver.find_element(By.XPATH,  '/html/body/div[1]/div[1]/main/form/div[1]/div/div/div[1]/div/div/div/div[2]/div/div[2]/div[2]/p')
    print(time.text)
else:
    print("No trip")
    
delay()
driver.back()

# earliest_trip_title = driver.find_element(By.XPATH,  '/html/body/div[1]/div[1]/main/div/div/section/div[2]/div/div[1]/div/div/div[1]/div/div[2]/div[1]/div[1]/strong')

# if(earliest_trip_title):
#     earliest_trip_time = driver.find_element(By.XPATH,  '/html/body/div[1]/div[1]/main/div/div/section/div[2]/div/div[1]/div/div/div[1]/div/div[2]/div[2]/strong')
#     trip_title_text = earliest_trip_title.text.encode('utf-8').decode('utf-8')
#     trip_time_text = earliest_trip_time.text.encode('utf-8').decode('utf-8')
#     print(trip_title_text + " ==> " + trip_title_text)
# else:
#     print("No trip")


time.sleep(5)  
driver.quit()