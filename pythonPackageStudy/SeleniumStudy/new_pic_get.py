from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://wiki.biligame.com/blhx/%E5%BD%B1%E7%94%BB%E7%9B%B8%E5%85%B3")

elements = driver.find_elements(By.CSS_SELECTOR, "#mw-content-text > div > center > ul > li")
for item in elements:
    item.find_element(By.TAG_NAME,"a").click()
    button = driver.find_element(By.CSS_SELECTOR,"a.mw-mmv-download-button")
    link = button.get_attribute("href")
    print(link)
    pic = requests.get(link)
    with open("./azure_lane_pic/" + link.split("/")[-1], "wb")as file:
        file.write(pic.content)
    driver.back()

driver.quit()

