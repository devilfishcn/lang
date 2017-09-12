# -*- coding: utf-8 -*-

with open('file.txt','a') as f:
    f.write('wxf')
    f.write('\n')
    f.write('wangxiaofei')
    f.write('\n')

with open('file.txt') as f:
    for line in f:
        print line