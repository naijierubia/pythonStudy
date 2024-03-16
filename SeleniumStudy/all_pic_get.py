from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time

driver = webdriver.Chrome()
new_page = webdriver.Chrome()
new_page.implicitly_wait(10)
driver.implicitly_wait(10)
driver.get("https://wiki.biligame.com/blhx/%E5%BD%B1%E7%94%BB%E7%9B%B8%E5%85%B3")

def click_switch():
    driver.find_element(By.CSS_SELECTOR, "#mc_accordion-1 > div:nth-child(3) > div.panel-heading > span > span.badge.pull-right").click()

click_switch()

elements = driver.find_elements(By.CSS_SELECTOR,"#mc_collapse-2 > ul > li")
i = 1
length = len(elements[399:])
for element in elements[399:]:
    print(f"{i}/{length}")
    link_1 = element.find_element(By.TAG_NAME,"a").get_attribute("href")
    new_page.get(link_1)
    link = new_page.find_element(By.CSS_SELECTOR,"div.mw-ui-button-group.mw-mmv-filepage-buttons > a.mw-mmv-view-expanded").get_attribute("href")
    response =requests.get(link)
    with open("./azure_lane_pic/"+link.split("/")[-1], "wb") as f:
        f.write(response.content)
        f.close()
    i += 1
driver.quit()