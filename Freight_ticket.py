#-*- coding: utf-8 -*-

from selenium import webdriver
from bs4 import BeautifulSoup
import re
import xlsxwriter

# 新建excle
ff = xlsxwriter.Workbook('Flight_Fee.xlsx')
ff_sheet = ff.add_worksheet()
title = ['Flight', 'Flight_Fee', 'Flight_Fee_Economy']
ff_sheet.write_row('A1', title)

# 抓取页面信息
in_city = 'sha'
out_city = 'pek'
in_date = '181212'
out_date = '181221'
url_xc = 'http://www.ceair.com/booking/' + in_city + '-' + out_city + '-' + in_date + '_CNY.html'
browser = webdriver.Chrome()
browser.get(url_xc)
browser.implicitly_wait(10)

# 提取页面信息，并写进exlce
soup = BeautifulSoup(browser.page_source)
browser.close()
soup_0 = soup.find(id = "sylvanas_0")
titles = soup.findAll(attrs = {"class" : "title"})
i = 2
for title in titles:
    Flight = re.findall(r'\|\xa0(.*?)<', str(title))
    print(Flight)
    row_num = 'A' + str(i)
    ff_sheet.write_row(row_num, Flight)
    i+=1

# times = soup.findAll(attrs = {"class" : "info clearfix"})
# for time in times:
#     print(time)
# details = soup.findAll(attrs = {"class" : "head cols-3"})
# for detail in details:
#     print(detail)

prices = soup.findAll(attrs={"class":"price luxury"})
i = 2
for price in prices:
    price = re.findall(r'</sub>(.*?)</dd>', str(price))
    print(price)
    row_num = 'B' + str(i)
    ff_sheet.write_row(row_num, price)
    i += 1

price_economys = soup.findAll(attrs={"class":"price economy"})
i = 2
for price_economy in price_economys:
    price_economy = re.findall(r'</sub>(.*?)</dd>', str(price_economy))
    print(price_economy)
    row_num = 'C' + str(i)
    ff_sheet.write_row(row_num, price_economy)
    i += 1

ff.close()