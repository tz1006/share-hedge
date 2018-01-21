#!/usr/bin/python3
# -*- coding: UTF-8 -*- 
# filename: data.py

from datetime import datetime
from random import choice

l = 3460
a = 0

def test():
    start_time = datetime.now()
    global d
    d = {}
    li = []
    for i in range(1, 3461):
        for l in range(1, 3461):
            if i != l:
                if int(i) < int(l):
                    text = '%s-%s' % (i,l)
                    if text not in li:
                        li.append(text)
                        d[text] = choice(range(1,11))
                        print(text)
                else:
                    text = '%s-%s' % (l,i)
                    if text not in li:
                        li.append(text)
                        d[text] = choice(range(1,11))
                        print(text)
    end_time = datetime.now()
    timedelsta = (end_time - start_time).seconds
    print('载入n条，耗时%d秒' % timedelsta)
    print(len(d))

import code
code.interact(banner = "", local = locals())
