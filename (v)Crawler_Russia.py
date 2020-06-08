#!/usr/bin/env python
# coding: utf-8

# In[1]:


import googletrans
import datetime
import pandas as pd
import datetime
import requests
from bs4 import BeautifulSoup

# 抓取網站
resource_url = 'https://www.mkrf.ru/press/announcement/'
re = requests.get(resource_url)
print(re.status_code)
# re.encoding = 'utf-8'
soup = BeautifulSoup(re.text, 'html.parser')
titledata = soup.find_all('div', class_='b-default__title')
datedata = soup.find_all('div', class_='b-article__date')
newslist = soup.find_all('div', class_='b-news-list')[0]
linklist = newslist.find_all('a')

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
        '發布機構':'俄羅斯聯邦文化部',
        '標題翻譯': title_zh,
        '標題原文': title,
        '連結':link
       }
df = pd.DataFrame(dict)

# 輸出csv
df.to_csv(r'C:\Users\User\Desktop\Result.csv', encoding = "utf_8_sig", mode = 'a', index = False)


# In[ ]:




