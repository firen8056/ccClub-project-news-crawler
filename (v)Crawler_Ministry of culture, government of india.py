from translate import Translator
import datetime
import pandas as pd
import datetime
import requests
from bs4 import BeautifulSoup

# 抓取網站
resource_url = 'http://www.indiaculture.nic.in/press-release'
re = requests.get(resource_url)
print(re.status_code)
soup = BeautifulSoup(re.text, 'html.parser')
data = soup.find_all('span', class_='field-content')

# 分類資訊
translator = Translator(to_lang='chinese')
title = []
title_zh = []
date = []
link = []
for i in range(0, len(data), 3):
    title.append(data[i].text.strip())
    zh_title = translator.translate(data[i].text.strip())
    title_zh.append(zh_title)
    try:
        link.append(data[i].a.get('href'))
    except:
        link.append('無連結')
for i in range(2, len(data), 3):
    date.append(data[i].text.strip())

# 組成表格
today = datetime.date.today()
dict = {'搜尋日期': today,
        '新聞日期': date,
        '地區別':'',
        '國家':'',
        '發布機構':'印度文化部',
        '標題翻譯': title_zh,
        '標題原文': title,
        '連結':link
       }
df = pd.DataFrame(dict)

# 輸出csv
df.to_csv(r'C:\Users\User\Desktop\Result.csv', encoding = "utf_8_sig", mode = 'a', index = False)
