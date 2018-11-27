#-*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

in_city = '上海'
out_city = '北京'
in_date = '2018-12-12'
out_date = '2018-12-21'
url_xc = 'http://flights.ctrip.com/?mkt_header=bdnm&AllianceID=108294&sid=767751&ouid=v1c5a1ss_VmJZMA86UGNRYgExBWQPPAAxB2VSIA==&popup=close&autoawaken=close&sourceid=2189'

browser = webdriver.Chrome()
browser.get(url_xc)
browser.find_element_by_id("DepartCity1TextBox").send_keys(in_city)
browser.find_element_by_id("DepartCity1TextBox").send_keys(Keys.ENTER)
browser.find_element_by_id("ArriveCity1TextBox").send_keys(out_city)
browser.find_element_by_id("ArriveCity1TextBox").send_keys(Keys.ENTER)
browser.find_element_by_id("DepartDate1TextBox").send_keys(in_date)
browser.find_element_by_id("DepartDate1TextBox").send_keys(Keys.ENTER)
print(browser.page_source)
browser.close()

# print(browser.current_url)
# print(browser.get_cookies())
# print(browser.page_source)
# browser.close()