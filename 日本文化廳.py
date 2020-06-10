#!/usr/bin/env python
# coding: utf-8

# In[1]:


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


# In[ ]:


# 分類資訊
translator = googletrans.Translator()
title, link, translate, date = [], [], [], []
for i in titledata:
    title.append(i.text.strip())
    link.append('https://www.bunka.go.jp' + (i.a.get('href')))
    result = translator.translate(i.text, src='ja', dest = 'zh-tw')
    title_zh.append(result.text)
for j in datedata:
    date.append(j.text.strip())

# 組成表格
today = datetime.date.today()
dict = {'搜尋日期': today,
        '新聞日期': date,
        '地區別':'',
        '國家':'',
        '發布機構':'日本文化廳',
        '標題翻譯': title_zh,
        '標題原文': title,
        '連結':link
       }
df = pd.DataFrame(dict)

# 輸出csv
df.to_csv(r'C:\Users\User\Desktop\Result.csv', encoding = "utf_8_sig", mode = 'a', index = False)

