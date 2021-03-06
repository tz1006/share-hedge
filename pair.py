#!/usr/bin/python3
# -*- coding: UTF-8 -*- 
# filename: pair.py

from tools import *
from sharelist_t import share_list
import threading
#import data
from datetime import datetime

count = 0
rate_1 = '0'
time = datetime.now()

def pair(code1, code2):
    global count
    global rate_1
    global time
    r = contrast(code1,code2)
    #print(code1, code2)
    if r[1] > 80:
        d['%s-%s' % (code1,code2)] = r[0]
    count += 1
    rate =  (float(count) / 5987530) * 100
    if str(rate).split('.')[1][0] != rate_1:
        timedelsta = (datetime.now() - time).total_seconds()
        rate_left = 100 - rate
        rate_1 = str(rate).split('.')[1][0]
        time = datetime.now()
        print('进度%d %%, 耗时%d秒, 预计还需%d小时。' % (round(str(rate), 3), timedelsta, round(timedelsta * 1000 / 3600, 3)))
    #print('%s %%' %rate)

def pair_t(code1, code2):
    global count
    r = contrast(code1,code2)
    #print(code1, code2)
    if r[1] > 80:
        d['%s-%s' % (code1,code2)] = r[0]
    rate =  (1 - (threading.activeCount() / 5987530)) * 100
    print('%s %%' %rate)

def test():
    #global start_time
    start_time = datetime.now()
    global d
    d = {}
    li = []
    for i in share_list:
        for l in share_list:
            if i != l:
                if int(i) < int(l):
                    text = '%s-%s' % (i,l)
                    if text not in li:
                        li.append(text)
                        pair(i,l)
                else:
                    text = '%s-%s' % (l,i)
                    if text not in li:
                        li.append(text)
                        pair(l,i)
    #d = sorted(d.items(), key=lambda d:d[0])
    end_time = datetime.now()
    timedelsta = (end_time - start_time).seconds
    print('载入n条，耗时%d秒' % timedelsta)

#test()


def test_t():
    start_time = datetime.now()
    global d
    d = {}
    li = []
    threads = []
    for i in share_list:
        for l in share_list:
            if i != l:
                if int(i) < int(l):
                    text = '%s-%s' % (i,l)
                    if text not in li:
                        li.append(text)
                        a = threading.Thread(target=pair_t, args=(i,l))
                        threads.append(a)
                        a.start()
                else:
                    text = '%s-%s' % (l,i)
                    if text not in li:
                        li.append(text)
                        a = threading.Thread(target=pair_t, args=(l,i))
                        threads.append(a)
                        a.start()
    for t in threads:
        t.join()
    #d = sorted(d.items(), key=lambda d:d[0])
    end_time = datetime.now()
    timedelsta = (end_time - start_time).seconds
    print('载入n条，耗时%d秒' % timedelsta)


import code
code.interact(banner = "", local = locals())

