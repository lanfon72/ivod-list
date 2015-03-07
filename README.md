# ivod-list
 parse `http://ivod.ly.gov.tw/` ，欄位為
 ```csv
 流水號,主辦單位,屆期,委員,發言時間,影片長度,會議時間,會議簡介,相關文檔(url)
 ```
 
# CC0 1.0 Universal License
  http://creativecommons.org/publicdomain/zero/1.0

# install dependencies
 Use **python2**, libs as below:
  - requests
  - bs4
 
# Running
```bash
python log.py <存檔位置> <起始流水號> <結束流水號>
```
 **parse 完的 csv 有少量 bug 待修正。
