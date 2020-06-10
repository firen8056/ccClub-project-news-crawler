import googletrans
import datetime
import time as t
import pandas as pd
import datetime
import requests
from bs4 import BeautifulSoup

# 抓取網站
resource_url = 'https://www.mkrf.ru/press/announcement/'
re = requests.get(resource_url)
print(re.status_code)
soup = BeautifulSoup(re.text, 'html.parser')
newslist = soup.find_all('div', class_='b-news-list')[0]
month = ['一','二','三','四','五','六','七','八','九','十','十一','十二']
day = ['一','二','三','四','五','六','七','八','九','十',
       '十一','十二', '十三','十四','十五','十六','十七','十八','十九','二十',
       '二十一','二十二', '二十三','二十四','二十五','二十六','二十七','二十八','二十九','三十','三十一']
yesterday = datetime.datetime.now() + datetime.timedelta(-1)
time1 = str(month[yesterday.month-1])+ '月' + str(day[yesterday.day-1]) + '日'
time2 = str(yesterday.month)+ '月' + str(yesterday.day) + '日'
print(time1)
print(time2)

# 分類及篩選資料
translator = googletrans.Translator()
title, link, translate, date = [], [], [], []

for i in newslist.find_all('a'):
    if translator.translate(i.find_all('div', class_='b-article__date')[0].text, src='ru', dest = 'zh-tw').text == time1 or translator.translate(i.find_all('div', class_='b-article__date')[0].text, src='ru', dest = 'zh-tw').text == time2:
        title.append(i.find_all('div', class_='b-default__title')[0].text)
        translate.append(translator.translate((i.find_all('div', class_='b-default__title')[0].text), src='ru', dest = 'zh-tw').text)
        link.append('https://www.mkrf.ru' + i.get('href'))
        date.append(translator.translate(i.find_all('div', class_='b-article__date')[0].text, src='ru', dest = 'zh-tw').text)
    else:
        continue
