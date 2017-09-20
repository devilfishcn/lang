# -*- coding: utf-8 -*-

from itertools import izip
from collections import defaultdict

for i in [0, 1, 2, 3, 4, 5]:
    print i**2

for i in range(6):
    print i**2
    
    
for i in xrange(6):
    print i**2
    
    
colors = ['red', 'green', 'blue', 'yellow']
for i in range(len(colors)):
    print colors[i]
    
for color in colors:
    print color
    
colors = ['red', 'green', 'blue', 'yellow']
for i in range(len(colors)-1, -1, -1):
    print colors[i]
    
for color in reversed(colors):
    print color
    
colors = ['red', 'green', 'blue', 'yellow']
for i in range(len(colors)):
    print i, '--->', colors[i]
    
for i, color in enumerate(colors):
    print i, '--->', color
    
names = ['raymond', 'rachel', 'matthew']
colors = ['red', 'green', 'blue', 'yellow']

n = min(len(names), len(colors))
for i in range(n):
    print names[i], '--->', colors[i]
    
for name, color in zip(names, colors):
    print name, '--->', color
    

for name, color in izip(names, colors):
    print name, '--->', color
    
    
colors = ['red', 'green', 'blue', 'yellow']

# 顺向排列
for color in sorted(colors):
    print colors
# 反向排列
for color in sorted(colors, reverse=True):
    print colors
    
colors = ['red', 'green', 'blue', 'yellow']
def compare_length(c1, c2):
    if len(c1) < len(c2): return -1
    if len(c1) > len(c2): return 1
    return 0

print sorted(colors, cmp=compare_length)


print sorted(colors, key=len)


d = {'matthew': 'blue', 'rachel': 'green', 'raymond': 'red'}

for k in d:
    print k
    
for k in d.keys():
    if k.startswith('r'):
            del d[k]
            
            
# Not very fast, has to re-hash every key and do a lookup
for k in d:
    print k, '--->', d[k]

# Makes a big huge list
for k, v in d.items():
    print k, '--->', v
    
for k, v in d.iteritems():
    print k, '--->', v
    

names = ['raymond', 'rachel', 'matthew']
colors = ['red', 'green', 'blue']

d = dict(izip(names, colors))
# {'matthew': 'blue', 'rachel': 'green', 'raymond': 'red'}

colors = ['red', 'green', 'red', 'blue', 'green', 'red']
# Simple, basic way to count. A good start for beginners.

d = {}
for color in colors:
    if color not in d:
         d[color] = 0
    d[color] += 1

# {'blue': 1, 'green': 2, 'red': 3}


d = {}
for color in colors:
     d[color] = d.get(color, 0) + 1

# Slightly more modern but has several caveats, better for advanced users
# who understand the intricacies

d = defaultdict(int)
for color in colors:
    d[color] += 1