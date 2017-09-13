# -*- coding: utf-8 -*-
names =['zhangsan','lisi','wangwu']
letters = [len(n) for n in names]#���ʽ��for �������� in �б�

longest_name = None
max_letters = 0

for i in range(len(names)):
    count = letters[i]
    if count > max_letters:
        longest_name = names[i]
        max_letters=count
print(longest_name)


for i,name in enumerate(names):
    count=letters[i]
    if count>max_letters:
        longest_name=name
        max_letters=count
print(longest_name)

for name,count in zip(names,letters):
    if count > max_letters:
        longest_name=name
        max_letters=count
print(longest_name)    