"""
Project: Smartphone Market Analysis

Description:
This script uses Selenium to automate Smartprix, load all smartphone listings,
and save the complete HTML page for further parsing with BeautifulSoup.

Author: Deepak Pathak
"""

from selenium import webdriver
import time
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://www.smartprix.com/mobiles")
time.sleep(2)


driver.find_element(by = By.XPATH, value = '//*[@id="app"]/main/aside/div/div[5]/div[2]/label[1]/input').click()
time.sleep(2)



oldd_height = driver.execute_script('return document.body.scrollHeight')

while True:
    driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/div[1]/div[2]/div/div[3]').click()
    time.sleep(1)

    neww_height = driver.execute_script('return document.body.scrollHeight')

    #print(oldd_height)
    #print(neww_height)

    if neww_height == oldd_height:
        break

    oldd_height = neww_height

html = driver.page_source

with open('smartprix.html', 'w', encoding = 'utf8') as f:
    f.write(html)

