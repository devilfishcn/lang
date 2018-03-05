# -*- coding: utf-8 -*-
import threading
import os
from  ConfigParser import ConfigParser
import redis
try:
    import cPickle as pickle
except ImportError:  
    import pickle

import json

from datetime import datetime
class EaseRedis():
    
    _instance_lock = threading.Lock()
    
    @staticmethod
    def instance():
        if not hasattr(EaseRedis, "_instance"):
            with EaseRedis._instance_lock:
                if not hasattr(EaseRedis, "_instance"):
                    # New instance after double check
                    EaseRedis._instance = EaseRedis()
        return EaseRedis._instance
    
    
    def __init__(self):
        root=os.path.dirname(os.path.realpath(__file__))
        parser=ConfigParser()
        parser.readfp(open(os.path.join(root,'redis.conf')))
        redis_conn = {'expire':0,'host':'','port':0,'db':0,'password':''}
        for key in redis_conn:
            if type(redis_conn[key]) == int:
                redis_conn[key] = int(parser.get('redis', key))
            else:
                redis_conn[key] = parser.get('redis', key)
        self.easeRedis=redis.StrictRedis(host = redis_conn['host'],port = redis_conn['port'],db = redis_conn['db'],password = redis_conn['password'])
        
        
easeRedis = EaseRedis().instance().easeRedis


# dict={'mother':'wangjingxiu'}
# str=json.dumps(dict)
# str='{''}'
# easeRedis.hset('familywang','persons',str)
lua = """
local value_list={}
if redis.call("HEXISTS", KEYS[1],KEYS[2]) == 1 then
    local value = redis.call('HGET',KEYS[1],KEYS[2])
    if type(value) == "string" then
    local box=cjson.decode('['..value..']')
    return box[1]['mother']
    end
else
    return 0
end 
"""

# lua = """
# local airlines={}
# for i,k in ipairs(KEYS) do
# table.insert(airlines,k)
# end
# for i,k in ipairs(ARGV) do
# table.insert(airlines,k)
# end
# return airlines
# """

    
multiply = easeRedis.register_script(lua)
  
print multiply(keys=['familywang','persons'], args=[6,7,8])




# 
# 
# 
# class ObjectDict(dict):
#     """Makes a dictionary behave like an object, with attribute-style access.
#     """
#     def __getattr__(self, name):
#         try:
#             return self[name]
#         except KeyError:
#             raise AttributeError(name)
# 
#     def __setattr__(self, name, value):
#         self[name] = value
#         
# class LoanUser(ObjectDict):
#     pass



# user =LoanUser()
# user.name='wxf'
# user.age=20
# user.address='beijing city'
# 
# 
# 
# 
# easeRedis.set('loan_user_info',pickle.dumps(user))
# data=easeRedis.get('loan_user_info')
# 
# new_user=pickle.loads(data)
# new_user.wife='李永瑾'
# new_user.date=datetime.now()
# easeRedis.set('loan_user_info',pickle.dumps(new_user))
# data=easeRedis.get('loan_user_info')
# new_user=pickle.loads(data)
# 
# print (new_user)
# print (new_user.wife)
# 
# user2 =LoanUser()
# if not hasattr(user2, "company"):
#     user2.company=u'heiniu公司'
# print user2.company































