#!/usr/bin/python3
# -*- coding: UTF-8 -*- 
# filename: data.py

from datetime import datetime
from random import chioce

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
    print(len(d))


import code
code.interact(banner = "", local = locals())
