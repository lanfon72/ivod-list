#!/usr/bin/env python
#coding:utf8
import sys
import requests, json, re
from bs4 import BeautifulSoup
from time import sleep

url = "http://ivod.ly.gov.tw/Play/VOD/"
# id from 1 to 79803
# id, 主辦單位, 屆期, 委員, 發言時間, 影片長度, 會議時間, 會議簡介, 相關文檔
# 
columns = [ "流水號", "主辦單位", "屆期", "委員", "發言時間", "影片長度", "會議時間", "會議簡介", "相關文檔" ]
sv = sys.argv[1]
f = open(sv,'wb+')
f.write(','.join(columns) + "\n")
print "===save on {}, start from {} to {}".format(sys.argv[1], sys.argv[2], sys.argv[3])
for uid in range(int(sys.argv[2]), int(sys.argv[3])):
    sleep(1)
    html = requests.get(url+str(uid))
    html.encoding = "utf8"
    soup = BeautifulSoup(html.text)
    content = soup.find("div",{"class":"video-text"})
    if not content:
        print ("ivod 網址編號 {0} 存取失敗.".format(uid))
        continue
    ptr = [str(uid)]
    ptr.append( content.find("h4").string.split(u"：")[1] )
    strs = [ _.getText() for _ in content.find_all("p") ]
    ptr.append( strs[1] ) #屆期
    ptr += [_.split(u"：")[1] for _ in strs[2:6]]
    ptr.append( strs[6].split(u"會議簡介：")[1].replace("\t",'').strip() ) #會議簡介
    href = content.find("a",href=True)
    if href:
        ptr.append( href["href"] ) #相關文檔

    f.write(",".join(ptr).encode('utf8') + "\n")
    ptr=[]
f.close()
