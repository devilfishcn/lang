# -*- coding: utf-8 -*-
from functools import partial
with open('file.txt','a') as f:
    f.write('wxf')
    f.write('\n')
    f.write('wangxiaofei')
    f.write('\n')

with open('file.txt') as f:
    for line in f:
        print line

with open('file.txt') as f:       
    blocks = []
    while True:
        block = f.read(32)
        if block == '':
                break
        blocks.append(block)
    print blocks
    
with open('file.txt') as f:    
    blocks = []
    for block in iter(partial(f.read, 32), ''):
        blocks.append(block)
    print blocks