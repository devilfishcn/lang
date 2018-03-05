
import tornado.gen
import tornado.web

import tornado.httpclient

import json
from time import sleep

from tornado.ioloop import IOLoop

#class MaindHandler(object):
    # http://www.cnblogs.com/apexchu/p/4226784.html
    # http://simple-is-better.com/news/1017
    
@tornado.gen.coroutine
def post():
        client = tornado.httpclient.AsyncHTTPClient()
        print '1'
        #resp =  yield client.fetch("http://47.92.104.74:8082/?module=API&method=Actions.getPageUrls&apiModule=UserCountry&apiAction=getCountry&idSite=1&period=day&date=2017-07-28&format=JSON&token_auth=f8148f87c9f60dd03f0b8b5ba35aba77&expanded=1&segment=actionUrl=@tuiaddcpc1")
        resp =  yield client.fetch("http://47.92.104.74:8082/?module=API&method=API.get&idSite=1&period=day&date=2017-07-28&format=JSON&token_auth=f8148f87c9f60dd03f0b8b5ba35aba77&segment=actionUrl=@tuiaddcpc1")
        print '2'
        if resp.code == 200:
            print resp.code
            resp = tornado.escape.json_decode(resp.body)
            print (json.dumps(resp, indent=4, separators=(',', ':')))
            
        else:
            print resp.code
            resp = {"message": "error when fetch something"}
            print(json.dumps(resp, indent=4, separators=(',', ':')))
            

def func_normal():
    print 'start'
    IOLoop.current().run_sync(lambda:post())
    print 'end'
    
func_normal()
