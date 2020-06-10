import googletrans
import datetime
import time as t
import pandas as pd
import datetime
import requests
from bs4 import BeautifulSoup

# 抓取網站
resource_url = 'https://www.soumu.go.jp/menu_news/s-news/index.html'
re = requests.get(resource_url)
print(re.status_code)
re.encoding = "SHIFT_JIS"
soup = BeautifulSoup(re.text, 'html.parser')
yesterday = datetime.datetime.now() + datetime.timedelta(-1)
time = str(yesterday.year) + '年' + str(yesterday.month)+ '月' + str(yesterday.day) + '日'
print(time)
table = soup.table
words = table.find_all('td')

# 分類篩選資訊
translator = googletrans.Translator()
title, link, translate, date = [], [], [], []
for i in range(0, len(words), 3):
    if words[i].text.strip() == time:
        date.append(words[i].text.strip())
        title.append(words[i+1].text.strip())
        link.append('https://www.soumu.go.jp' + (words[i+1].a.get('href')))
        translate.append(translator.translate(words[i+1].text, src='ja', dest = 'zh-tw').text)
    else:
        continue
