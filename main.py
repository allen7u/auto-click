













from datetime import datetime
from selenium import webdriver

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.options import Options

import time


# attach to openned chrome

chrome_options = Options()

chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
# chrome_options.add_argument("--remote-debugging-port=9222")


driver = webdriver.Chrome(chrome_options=chrome_options)

while True:
    if datetime.now() > datetime.strptime("2022-11-02 00:11:30", "%Y-%m-%d %H:%M:%S"):
        print("Time is up!")
        break

# driver.get("https://www.google.com")
driver.get("https://h5.m.taobao.com/cart/order.html?itemId=657214842391&item_num_id=657214842391&_input_charset=utf-8&buyNow=true&v=0&skuId=4916023075351&quantity=1")

# button = WebDriverWait(driver, 10, 0.01).until(EC.presence_of_element_located((By.TAG_NAME, 'input')))
button = WebDriverWait(driver, 10, 0.01).until(EC.presence_of_element_located((By.XPATH, '//*[@id="submitBlock_1"]/div/div/div/div[3]')))

button.click()

xxx

# search_box = driver.find_element( By.XPATH, '//*[@id="submitBlock_1"]/div/div/div/div[3]')

# print(search_box.text)

# search_box.click()



# print page title

# print(driver.title)

# print page source

# print(driver.page_source)

# search_box = driver.find_elements( By.TAG_NAME, "div")

# search_box = driver.find_element( By.PARTIAL_LINK_TEXT, "提交订单")
# search_box = driver.find_element( By.XPATH, '//*[@id="submitBlock_1"]/div/div/div/div[3]/div[2]/span')

# print(search_box.text)

# search_box.click()


# for i in search_box:

#     print(i.text)

# print(search_box)

xxx

driver.get("https://www.google.com")

search_box = driver.find_element( By.TAG_NAME, "input")

# type in the search

search_box.send_keys("selenium")

# hit return after you enter search text

search_box.send_keys(Keys.RETURN)

# you should see "No results found." on the page


