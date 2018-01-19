#!/usr/bin/python3
# -*- coding: UTF-8 -*- 
# filename: trend.py

import requests
from tools import *
from sharelist_t import share_list

s = requests.session()
s.keep_alive = False

def dic_hist(code, day=100):
    url = 'http://api.finance.ifeng.com/akdaily/?code=%s&type=last' % sscode(code)
    r = s.get(url)
    d = {}
    li = r.json()['record']
    if len(li) < 100:
        print('%s少于100天' % code)
        return(d)
    else:
        for i in range(100):
            i = i + 1
            date = li[-i][0]
            wave = float(li[-i][7])
            #如果跌幅超过百分之5
            if -5 < wave:
                t = 1
            #如果涨幅超过百分之5
            elif wave > 5:
                t = 2
            else:
                t = 0
            d[date] = t
        return(d)


    
    #如果跌幅超过百分之5
    if -5 < wave:
        t = '1'
    #如果涨幅超过百分之5
    elif wave > 5:
        t = '2'
    else:
        t = '0'
    g += t
if len(li) < 734:
    for i in range(734-len(li)):
        g+
        
        
from sharelist_t import share_list
for i in share_list:
    url = 'http://api.finance.ifeng.com/akdaily/?code=%s&type=last' % sscode(i)
    r = s.get(url)
    li = r.json()['record']
    if len(li) > 734:
        print('-' + i)
        print(len(li))
