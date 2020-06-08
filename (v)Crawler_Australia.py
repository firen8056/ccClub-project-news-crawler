from translate import Translator
import datetime
import pandas as pd
import datetime
import requests
from bs4 import BeautifulSoup

# 抓取網站
resource_url = 'https://www.dlgsc.wa.gov.au/department/news/-in-category/categories/culture-and-the-arts'
re = requests.get(resource_url)
print(re.status_code)
soup = BeautifulSoup(re.text, 'html.parser')
# allnews = soup.find('div', class_='newsCardListing')
titledata = soup.find_all('h3')
datedata = soup.find_all('span', class_='text-muted')
    
# 分類資訊
translator = Translator(to_lang='chinese')
title = []
title_zh = []
date = []
link = []
for i in titledata:
    title.append(i.text.strip())
    link.append((i.a.get('href')))
    zh_title = translator.translate(i.text.strip())
    title_zh.append(zh_title)
for j in datedata:
    date.append(j.text.strip())

# 組成表格
today = datetime.date.today()
dict = {'搜尋日期': today,
        '新聞日期': date,
        '地區別':'',
        '國家':'',
        '發布機構':'西澳地方政府體育與文化產業部門',
        '標題翻譯': title_zh,
        '標題原文': title,
        '連結':link
       }
df = pd.DataFrame(dict)

# 輸出csv
df.to_csv(r'C:\Users\User\Desktop\Result.csv', encoding = "utf_8_sig", mode = 'a', index = False)
