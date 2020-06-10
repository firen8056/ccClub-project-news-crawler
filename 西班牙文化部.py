import googletrans
import datetime
import time as t
import pandas as pd
import datetime
import requests
from bs4 import BeautifulSoup

# 抓取網站
resource_url = 'https://www.culturaydeporte.gob.es/portada.html'
re = requests.get(resource_url)
print(re.status_code)
soup = BeautifulSoup(re.text, 'html.parser')
list = soup.find_all('div', class_='enlace')
time = (datetime.date.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')

# 分類及篩選資料
translator = googletrans.Translator()
title, link, translate, date = [], [], [], []

for i in list:
    if i.find_all('span', class_='fecha')[0].text == time:
        title.append(i.find_all('p', class_='titulo')[0].text.strip())
        date.append(i.find_all('span', class_='fecha')[0].text)
        translate.append(translator.translate(i.find_all('p', class_='titulo')[0].text, src='es', dest = 'zh-tw').text)
        link.append('https://www.culturaydeporte.gob.es' + (i.a.get('href')))
    else:
        continue
