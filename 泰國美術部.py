#!/usr/bin/env python
# coding: utf-8

# In[8]:


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

print(date)


# In[ ]:


# 分類資訊
translator = googletrans.Translator()
title = []
title_zh = []
date = []
link = []
for i in titledata:
    title.append(i.text.strip())
    result = translator.translate(i.text, src='ru', dest = 'zh-tw')
    title_zh.append(result.text)
for j in datedata:
    datetranslate = translator.translate(j.text, src='ru', dest = 'zh-tw')
    date.append(datetranslate.text.strip())
for k in linklist:
    link.append('https://www.mkrf.ru' + k.get('href'))
    
# 組成表格
today = datetime.date.today()
dict = {'搜尋日期': today,
        '新聞日期': date,
        '地區別':'',
        '國家':'',
        '發布機構':'',
        '標題翻譯': title_zh,
        '標題原文': title,
        '連結':link
       }
df = pd.DataFrame(dict)

# 輸出csv
df.to_csv(r'C:\Users\User\Desktop\Result.csv', encoding = "utf_8_sig", mode = 'a', index = False)

