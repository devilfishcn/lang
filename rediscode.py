# -*- coding: utf-8 -*-

# 模块与包的区别

# import redis
# r = redis.Redis(host='121.40.176.186',port=6379,password='dd8mj1',db=0)
# r.set('name', 'wxf')
# print(r.get('name'))


# from redis import Redis
# r = Redis(host='121.40.176.186',port=6379,password='dd8mj1',db=0)
# print(r.get('name'))



from redis import Redis
r = Redis(host='47.94.206.52',port=6379,password='wxf1983',db=0)
r.set('name', 'wxf')
print r.get('name')