#!/usr/bin/env python3
#! -*- encoding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import json,requests,sys,os
#獲取公網ip
html=requests.get("http://localhost:4040/api/tunnels").text
tunnel_data=json.loads(html)
server_address=tunnel_data["tunnels"][0]["public_url"]
#獲取config
config_file=open(os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])),"Selenium-config.json"),"r")
config_data=json.load(config_file)
url="https://my.freenom.com/clientarea.php?action=domaindetails&id=1117076905&modop=custom&a=urlforwarding"
browser=webdriver.Safari()
#訪問網頁
browser.maximize_window()
browser.get(url)
#登入
browser.find_element_by_id("username").send_keys(config_data["account"])
browser.find_element_by_id("password").send_keys(config_data["password"])
browser.find_element_by_xpath("//input[@value='Login']").click()
#first(在10秒內等待網頁元素的加載，若逾時則回報錯誤)
locator = (By.ID, "url")  # 定位器
search_input = WebDriverWait(browser, 20).until(EC.presence_of_element_located(locator),"failed")
if search_input!="failed":
    browser.find_element_by_id("url").send_keys(server_address)
    search_input=0
else:
    print(search_input)
    exit(0)
browser.find_element_by_xpath("//input[@value='Set URL']").click()
browser.quit()
print("Done!")
