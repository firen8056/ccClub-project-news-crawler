import googletrans
import datetime
import time as t
import pandas as pd
import datetime
import requests
from bs4 import BeautifulSoup

# 抓取網站
resource_url = 'https://www.finearts.go.th/main/categorie/general-news'
re = requests.get(resource_url)
print(re.status_code)
soup = BeautifulSoup(re.text, 'html.parser')
month = ['一','二','三','四','五','六','七','八','九','十','十一','十二']
yesterday = datetime.datetime.now() + datetime.timedelta(-1)
time = str(month[yesterday.month-1])+ '月' + (datetime.date.today() - datetime.timedelta(days=1)).strftime('%d')
print(time)
newslist = soup.find_all('div', class_='card col-md-4 col-sm-12 col-xs-12')

# 分類篩選資訊
translator = googletrans.Translator()
title, link, translate, date = [], [], [], []

for i in newslist:
    if i.find_all('div', class_='month_') == []:
        continue
    elif str(translator.translate(i.find_all('div', class_='month_')[0].text, dest = 'zh-tw').text) + str(i.find_all('div', class_='day_')[0].text) == time:
        date.append(str(translator.translate(i.find_all('div', class_='month_')[0].text, dest = 'zh-tw').text) + str((i.find_all('div', class_='day_')[0].text)))
        title.append(i.find_all('h5', class_='card-title _limitrow1')[0].text.strip())
        translate.append(translator.translate(i.find_all('h5', class_='card-title _limitrow1')[0].text, dest = 'zh-tw').text)
        link.append('https://www.mkrf.ru' + i.a.get('href'))
    else:
        continue
