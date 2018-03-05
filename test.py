# _*_ coding: utf-8 _*_


# time_zone ='xxx'
# init_command='SET time_zone = "%s"' % time_zone
# print init_command
# 
# 
# 'xxyz'
# 1+1


# from threading import Timer  
# import time  
#   
# timer_interval=10  
# 
# class person():
#     def __init__(self,name):
#         self.name=name
#         
#     def say(self):  
#         print 'i m ',self.name  
# 
# person=person('wxf')
# 
# t=Timer(timer_interval,person.say())  
# t.start() 
# t.setDaemon(True)

# from tornado import gen
# from tornado.httpclient import AsyncHTTPClient
# from tornado.ioloop import IOLoop
# 
# 
# # class a(object):
# #     
# #     @gen.coroutine
# #     def vist(self,i):
# #     #     client=AsyncHTTPClient()
# #     #   response = yield client.fetch("https://www.baidu.com")
# #     #   print response.body
# #         self.s = yield xx(i)
# #         self.y =yield xx(i)
# # @gen.coroutine         
# # def xx(i):
# #     raise gen.Return(i)
# # 
# # # m=vist()
# # # print m.result()
# # x= a()
# # 
# # # IOLoop.current().run_sync(lambda:x.vist(10))
# # # print x.s,x.y
# # 
# # x.vist(10)
# # print x.s,x.y
# 
# 

# 
# a=u'中国'
# b='china'
# print type(a),type(b)
# print a
# print a.encode('utf-8')
# from tornado.escape import utf8
# url=None
# print utf8(None)



import json


s='{"a":"a"}'
d={'c':'c'}

d.update(s)


a_str='{"a":"a"}'
b_dict={'b':'b'}

b_dict.update(a_str)








































