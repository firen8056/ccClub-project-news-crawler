#!/usr/bin/env python
# coding: utf-8

# In[6]:


from translate import Translator
import datetime
import pandas as pd
import datetime
import requests
from bs4 import BeautifulSoup

# 抓取網站
resource_url = 'https://www.lcsd.gov.hk/clpss/tc/webApp/News.do'
re = requests.get(resource_url)
print(re.status_code)
soup = BeautifulSoup(re.text, 'html.parser')
table = soup.tbody
content = table.find_all('td')

# 分類資訊
title = []
date = []
link = []
for i in range(1, len(content), 2):
    title.append(content[i].text.strip())
    a = content[i].find('input', {'type': 'hidden'}).get('value')
    link.append('https://www.lcsd.gov.hk/clpss/tc/webApp/NewsDetails.do?id=' + a)
for j in range(0, len(content), 2):
    date.append(content[j].text.strip())


# 組成表格
today = datetime.date.today()
dict = {'搜尋日期': today,
        '新聞日期': date,
        '地區別':'',
        '國家':'',
        '發布機構':'香港特別行政區康樂及文化事務署',
        '標題翻譯': title,
        '標題原文': title,
        '連結':link
       }
df = pd.DataFrame(dict)

# 輸出csv
df.to_csv(r'C:\Users\User\Desktop\Result.csv', encoding = "utf_8_sig", mode = 'a', index = False)


# In[ ]:





# In[ ]:




