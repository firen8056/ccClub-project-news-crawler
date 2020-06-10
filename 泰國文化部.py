#!/usr/bin/env python
# coding: utf-8

# In[26]:


import googletrans
import datetime
import time as t
import pandas as pd
import datetime
import requests
from bs4 import BeautifulSoup

# 抓取網站
resource_url = 'http://www.m-culture.go.th/en/more_news.php?cid=1'
re = requests.get(resource_url)
print(re.status_code)
soup = BeautifulSoup(re.text, 'html.parser')
time = (datetime.date.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
newslist = soup.find_all('div', class_='newsall-work-wrap newsall-comments')

# 分類篩選資訊
translator = googletrans.Translator()
title, link, translate, date = [], [], [], []

for i in newslist:
    if i.find_all('p', class_='icon-purple')[1].text.strip() == time:
        title.append(i.h4.text.strip())
        translate.append(translator.translate(i.h4.text.strip(), dest = 'zh-tw').text)
        date.append(i.find_all('p', class_='icon-purple')[1].text.strip())
        link.append('http://www.m-culture.go.th/en/' + i.a.get('href'))
    else:
        continue


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

