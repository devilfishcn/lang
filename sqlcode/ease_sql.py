# -*- coding: utf-8 -*-
import threading
import os
from  ConfigParser import ConfigParser
import redis
try:
    import cPickle as pickle
except ImportError:  
    import pickle
from datetime import datetime
import torndb 
from objectutils import DBRecord
import json

class EaseSQLServer():
    
    _instance_lock = threading.Lock()
    
    @staticmethod
    def instance():
        if not hasattr(EaseSQLServer, "_instance"):
            with EaseSQLServer._instance_lock:
                if not hasattr(EaseSQLServer, "_instance"):
                    # New instance after double check
                    EaseSQLServer._instance = EaseSQLServer()
        return EaseSQLServer._instance
    
    
    def __init__(self):
        root=os.path.dirname(os.path.realpath(__file__))
        parser=ConfigParser()
        parser.readfp(open(os.path.join(root,'sql.conf')))
        sql_conn = {'host':'','db':'','user':'','password':''}
        for key in sql_conn:
                sql_conn[key] = parser.get('sqlserver', key)
        self.easeSQLServer=torndb.Connection(host = sql_conn['host'],database = sql_conn['db'],user = sql_conn['user'],password = sql_conn['password'])
        
        
def insert_by_dict(conn, tablename, rowdict, replace=False):
    cursor = conn._cursor()
    cursor.execute("describe %s" % tablename)
    allowed_keys = set(row[0] for row in cursor.fetchall())
    keys = allowed_keys.intersection(rowdict)

    if len(rowdict) > len(keys):
        unknown_keys = set(rowdict) - allowed_keys

    columns = ", ".join(keys)
    values_template = ", ".join(["%s"] * len(keys))

    if replace:
        sql = "REPLACE INTO %s (%s) VALUES (%s)" % (
            tablename, columns, values_template)
    else:
        sql = "INSERT INTO %s (%s) VALUES (%s)" % (
            tablename, columns, values_template)
        
    values = tuple(rowdict[key] for key in keys)
    try:
        cursor.execute(sql, values)
        
        return cursor.lastrowid
    finally:
        cursor.close()
        
conn = EaseSQLServer().instance().easeSQLServer

# mobile='13691036309'
# result=conn.get('select * from t_loan_mobiles where mobile=%s',mobile)
# print result



# record=DBRecord()
# record.idNo='130124198312063310'
# record.mobile='1369106'
# rowid=insert_by_dict(conn,'t_ease_tbl',record)
# print rowid


# result=conn.query('select mobile from t_ease_tbl')
# print json.dumps(result)

# print json.dumps(datetime.now())
# result=conn.get('select * from t_ease_tbl where mobile=%s','136xx')
# print result.name
# name =  json.loads(result.name)
# print name
# name['city']=u'北京'
# print json.dumps(name, ensure_ascii=False).decode('utf8')







# --建立表格的内容
# DROP TABLE IF EXISTS `t_ease_tbl`;
# CREATE TABLE `t_ease_tbl` (
#   `id` bigint(20) NOT NULL AUTO_INCREMENT,
#   `idNo` varchar(20) DEFAULT NULL,
#   `name` varchar(60) DEFAULT NULL,
#     `mobile` varchar(11) DEFAULT NULL,
#   `sex` varchar(4) DEFAULT NULL,
#   `birth` varchar(20) DEFAULT NULL,
#   `age` smallint(6) DEFAULT NULL,
#   `create_time` datetime DEFAULT NULL,
#   `update_time` datetime DEFAULT NULL,
#    PRIMARY KEY (`id`),
#    UNIQUE KEY `mobile` (`mobile`)
# )  ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;














record=DBRecord()
# record.name='王晓飞'
# record.sex='m'
# record.birth='1983-12-06'
# record.age=30
# record.phone='mobile'
# record.ip='127.0.0.1'
# record.city='北京'
# record.amount=500
# record.subchannel=''
# record.agree=''
# record.credit=''
# record.custom=''

# record.mobile='13691036309'
# record.create_time=datetime.now()
# record.update_time=datetime.now()
# 
# 
# insert_by_dict(conn, 't_loan_mobiles', record)






sql='update t_loan_mobiles set verify_status = %s , update_time = %s , verify_time= %s where mobile=%s'
status=0
update_time=verify_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
phone='13691036309'
conn.execute(sql,status,update_time,verify_time,phone)






























