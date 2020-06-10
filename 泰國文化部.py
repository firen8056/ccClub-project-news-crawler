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
