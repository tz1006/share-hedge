#!/usr/bin/python3
# -*- coding: UTF-8 -*- 
# filename: pair.py

from tools import *
from sharelist_t import share_list
import threading

def pair(code1, code2):
    r = contrast(code1,code2)
    print(code1, code2)
    if r[1] > 80:
        d['%s-%s' % (code1,code2)] = r[2]


def test():
    global d
    d = {}
    li = []
    for i in share_list:
        for l in share_list:
            if i != l:
                if int(i) > int(l):
                    text = '%s-%s' % (i,l)
                else:
                    text = '%s-%s' % (l,i)
                if text not in li:
                    li.append(text)
                    target=pair(i,l)
    d = sorted(d.items(), key=lambda d:d[0])
    print('Finish')

#test()


def test_t():
    global d
    d = {}
    li = []
    threads = []
    for i in share_list:
        for l in share_list:
            if i != l:
                if int(i) > int(l):
                    text = '%s-%s' % (i,l)
                else:
                    text = '%s-%s' % (l,i)
                if text not in li:
                    li.append(text)
                    a = threading.Thread(target=pair, args=(i,l))
                    threads.append(a)
                    a.start()
    for t in threads:
        t.join()
    d = sorted(d.items(), key=lambda d:d[0])
    print('Finish')

