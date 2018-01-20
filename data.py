#!/usr/bin/python3
# -*- coding: UTF-8 -*- 
# filename: data.py

from tools import *
from sharelist_t import share_list
import json
import threading
from datetime import datetime

def dl_json(code):
    j = ma_hist(code, 10, 1).json()
    with open("json/%s.json" % code,"w") as f:
        json.dump(j,f)
    #f.close()

def ld_json(code):
    with open("json/%s.json" % code,'r') as load_f:
        j = json.load(load_f)
    return(j)

def download():
    print('正在载入历史数据到json')
    start_time = datetime.now()
    threads = []
    for i in share_list:
        a = threading.Thread(target=dl_json,args=(i,))
        threads.append(a)
        a.start()
    for t in threads:
        t.join()
    end_time = datetime.now()
    timedelsta = (end_time - start_time).seconds
    print('载入%d条，耗时%d秒' %(len(share_list), timedelsta))

download()
# ulimit -n 5000
