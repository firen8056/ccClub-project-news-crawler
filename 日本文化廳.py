import googletrans
import datetime
import time as t
import pandas as pd
import datetime
import requests
from bs4 import BeautifulSoup

# 抓取網站
resource_url = 'https://www.bunka.go.jp/whats_new.html'
re = requests.get(resource_url)
print(re.status_code)
re.encoding = 'utf-8'
soup = BeautifulSoup(re.text, 'html.parser')
newslist = soup.find_all('ul', class_='news_list_tag')
yesterday = datetime.datetime.now() + datetime.timedelta(-1)
time = str(yesterday.year) + '年' + str(yesterday.month)+ '月' + str(yesterday.day) + '日'
print(time)
everylist = newslist[0].find_all('li')

# 分類篩選資訊
translator = googletrans.Translator()
title, link, translate, date = [], [], [], []
for i in everylist:
    if i.find_all('p', class_='news_list_date')[0].text == time:
        title.append(i.find_all('p', class_='news_list_ttl')[0].text)
        link.append('https://www.bunka.go.jp' + (i.a.get('href')))
        translate.append(translator.translate(i.find_all('p', class_='news_list_ttl')[0].text, src='ja', dest = 'zh-tw').text)
        date.append(i.find_all('p', class_='news_list_date')[0].text)
    else:
        continue
