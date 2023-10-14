# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome import service
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC


def main():
    sr = Service('D:\\uniSource\\software testing\\project\\selenium\\chromedriver-win64\\chromedriver.exe')
    options = Options()
    options.binary_location = "C:\\Users\\Hosseintrz\\Downloads\\Compressed\\chrome-win64\\chrome-win64\\chrome.exe"
    driver = webdriver.Chrome(service=sr, options=options)
    driver.implicitly_wait(6)
    driver.get("https://torob.com/")
    elem = driver.find_element(By.NAME, "query")
    elem.send_keys("لپتاپ ایسوس")
    elem.send_keys(Keys.ENTER)

    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="layout-wrapp"]/div[2]/div/div/div[2]/div[3]/div/div')))

    print("cards loaded")
    time.sleep(1)
    print("continuing")
    #product_items = driver.find_elements(By.XPATH, "jsx-2514672dc9197d80")
    product_items = driver.find_element(
        By.XPATH, '//*[@id="layout-wrapp"]/div[2]/div/div/div[2]/div[3]/div/div'
    ).find_elements(By.XPATH, "./*")

    trans_table = str.maketrans(
        '۰۱۲۳۴۵۶۷۸۹',
        '0123456789'
    )

    products = {}
    print("count products : ", len(product_items))
    for item in product_items:
        product_name = item.find_element(By.CLASS_NAME, "product-name") .text
        product_price = item.find_element(
            By.XPATH,
            './a/div/div[3]'
            #'//*[@id="layout-wrapp"]/div[2]/div/div/div[2]/div[3]/div/div/div[62]/a/div/div[3]'
        ).text
#        product_price = item.find_element(By.CLASS_NAME, "product-price-text").text

        product_price = ''.join(filter(str.isdigit, product_price))
        product_price = product_price.translate(trans_table)
        print(product_name, "--")
        print(product_price)

        products[product_name] = product_price

    arr = sorted(products.items(), key=lambda item: int(item[1]))
    cheapest_item = arr[0]
    print("-----------------------------")
    print("cheapest lenovo laptop: ", cheapest_item[0])
    print("price: ", cheapest_item[1])

    print("finished")
    driver.close()


if __name__ == '__main__':
    main()

