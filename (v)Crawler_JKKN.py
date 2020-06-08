#!/usr/bin/env python
# coding: utf-8

# In[3]:


import googletrans
import datetime
import pandas as pd
import datetime
import requests
from bs4 import BeautifulSoup

# 抓取網站
resource_url = 'http://www.jkkn.gov.my/en/press-releases'
re = requests.get(resource_url)
print(re.status_code)
soup = BeautifulSoup(re.text, 'html.parser')
titledata = soup.find_all('span', class_='field-content')
datedata = soup.find_all('span', class_='date')
linkdata = soup.find_all('span', class_='file')

# 分類資訊
translator = googletrans.Translator()
title = []
title_zh = []
date = []
link = []
for i in titledata:
    title.append(i.text.strip())
    zh_title = translator.translate(i.text.strip(), src = 'ms', dest = 'zh-tw')
    title_zh.append(zh_title.text)
for j in datedata:
    date.append(j.text.strip())
for k in linkdata:
    link.append(k.a.get('href'))

# 組成表格
today = datetime.date.today()
dict = {'搜尋日期': today,
        '新聞日期': date,
        '地區別':'',
        '國家':'',
        '發布機構':'馬來西亞國家文化與藝術局',
        '標題翻譯': title_zh,
        '標題原文': title,
        '連結':link
       }
df = pd.DataFrame(dict)

# 輸出csv
df.to_csv(r'C:\Users\User\Desktop\Result.csv', encoding = "utf_8_sig", mode = 'a', index = False)


# In[6]:





# In[ ]:




