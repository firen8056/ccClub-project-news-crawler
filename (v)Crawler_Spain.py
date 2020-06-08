import googletrans
import datetime
import pandas as pd
import datetime
import requests
from bs4 import BeautifulSoup

# 抓取網站
resource_url = 'https://www.culturaydeporte.gob.es/portada.html'
re = requests.get(resource_url)
print(re.status_code)
soup = BeautifulSoup(re.text, 'html.parser')
titledata = soup.find_all('div', class_='enlace')
datedata = soup.find_all('span', class_='fecha')

# 分類資訊
translator = googletrans.Translator()
title = []
title_zh = []
date = []
link = []
for i in titledata:
    title.append(i.p.text.strip())
    link.append('https://www.culturaydeporte.gob.es' + (i.a.get('href')))
    result = translator.translate(i.p.text.strip(), src='es', dest = 'zh-tw')
    title_zh.append(result.text)
for j in datedata:
    date.append(j.text.strip())

# 組成表格
today = datetime.date.today()
dict = {'搜尋日期': today,
        '新聞日期': date,
        '地區別':'',
        '國家':'',
        '發布機構':'西班牙文化部',
        '標題翻譯': title_zh,
        '標題原文': title,
        '連結':link
       }
df = pd.DataFrame(dict)

# 輸出csv
df.to_csv(r'C:\Users\User\Desktop\Result.csv', encoding = "utf_8_sig", mode = 'a', index = False)
