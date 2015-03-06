#!usr/bin/env python
#coding:utf8
import requests, json, re
from bs4 import BeautifulSoup
from time import sleep
url = "http://ivod.ly.gov.tw/Play/VOD/"
# id from 1 to 79803
# id, 主辦單位, 屆期, 委員, 發言時間, 影片長度, 會議時間, 會議簡介, 相關文檔
# 
columns = [ "id", u'主辦單位', u'屆期', u'委員', u'發言時間', u'影片長度', u'會議時間', u'會議簡介', u'相關文檔' ]
points = []
for uid in range(1,50):
    sleep(1)
    html = requests.get(url+`uid`)
    html.encoding = "utf8"
    soup = BeautifulSoup(html.text)
    content = soup.find("div",{"class":"video-text"})
    if not content:
        print u"ivod 網址編號 {0} 存取失敗.".format(uid)
        continue
    ptr = [uid]
    ptr.append( content.find('h4').string.split(u"：")[1] )
    strs = [ _.getText() for _ in content.find_all('p') ]
    ptr.append( strs[1] ) #屆期
    [ptr.append(_.split(u"：")[1]) for _ in strs[2:6] ]
    ptr.append( strs[6] ) #會議簡介
    href = content.find('a',href=True)
    if href:
        ptr.append( href['href'] ) #相關文檔
    print json.dumps({k:v for k,v in zip(columns,ptr)}, ensure_ascii=False, sort_keys=True)
    points.append(ptr)
    ptr=[]
