import requests

#获取页面数据html
url = r"https://comment.bilibili.com/92542241.xml"
r = requests.get(url)#访问url
r.encoding="utf-8"

from bs4 import BeautifulSoup
#解析页面
soup = BeautifulSoup(r.text,'lxml')#lxml是常用的解析器，需要提前使用pip工具安装lxml库
d = soup.find_all("d")#找到所有页面的d标签
#print(d)

import datetime
#解析弹幕，将弹幕、网址、时间整理为字典，最后加和成列表，共1000条
dlst = []
n = 0
for i in d:
    n += 1
    danmuku = {}#将单条数据装进字典
    danmuku['弹幕'] = i.text
    danmuku['网址'] = url
    danmuku['时间'] = datetime.date.today()#需要导入datetime库
    dlst.append(danmuku)#将所有的字典装进一个列表
    print("获取了%d条数据" %n)
#print(dlst)

import pandas as pd
#将列表变为DateFrame，使用pandas进行分析
df = pd.DataFrame(dlst).to_excel('b站弹幕数据.xlsx')
#df.to_excel('b站弹幕数据.xlsx')#爬取下来的数据放在excel里


