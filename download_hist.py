#!/usr/bin/python3
# -*- coding: UTF-8 -*- 
# filename: download_hist.py

from tools import *
from sharelist_t import share_list
import json
import threading

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
    threads = []
    for i in share_list:
        a = threading.Thread(target=dl_json,args=(i,))
        threads.append(a)
        a.start()
    for t in threads:
        t.join()
    print('loaded!')

download()
# ulimit -n 5000
