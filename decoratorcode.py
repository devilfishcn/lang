# -*- coding: utf-8 -*-
# def bread(func):
#     def wrapper():
#         print "</''''''\>"
#         func()
#         print "</______\>"
#     return wrapper
# @bread
# def sandwich(food="--ham--"):
#     print food   
# sandwich()

#下面为简单的装饰器函数
from time import ctime
# def deco(func):#函数对象
#     def decorator(*args,**kwargs):
#         print('[%s] %s() is called' % (ctime(),func.__name__))
#         return func(*args,**kwargs)
#     return decorator
# @deco
# def foo():
#     print('hello,python')
#     
# foo()# foo=deco(foo)


#嵌套的装饰器函数

# def deco1(func):#函数对象
#     def decorator1(*args,**kwargs):
#         print('[%s] %s() is called' % (ctime(),func.__name__))
#         return func(*args,**kwargs)
#     return decorator1
# 
# 
# def deco2(func):#函数对象
#     def decorator2(*args,**kwargs):
#         print('[%s] %s() is called' % (ctime(),func.__name__))
#         return func(*args,**kwargs)
#     return decorator2
# 
# @deco2
# @deco1
# def foo():
#     print('hello,python')
# 
# foo()

#传递参数的装饰器
def deco(tag):
    def decorator(func):
        def wrapper(*args,**kwargs):
            print('[%s] %s() is called, tag is %s.' % (ctime(),func.__name__,tag))
            return func(*args,**kwargs)
        return wrapper
    return decorator
@deco('python')
def foo():
    print('hello python')

@deco('java')
def bar():
    print('hello pathon')

foo()
bar()

