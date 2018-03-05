# # def func():
# #     yield 1
# #     yield 2
# #     yield 3
# #     yield 4
# #     yield 5
# #     yield 6
# #     yield 7
# #     
# # f=func()   
# # print next(f)
# # print next(f)
# # print next(f)
# # print next(f)
# 
# import functools
# 
# 
# def wxf(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print args[0].name
#         result = func(*args, **kwargs)
#         print result
#         return result
#     return wrapper
# 
# 
# class student():
#     
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     @wxf    
#     def sayHello(self,name):
#         print name,self.age
# 
# 
# 
# 
# 
# 
# s=student('wxf',20)
# s.sayHello('vip')
# 
# 
# 
# 
# # @wxf
# # def function(i):
# #     
# #     print i
# #     return 100
# #     
# #     
# # function(1)






































