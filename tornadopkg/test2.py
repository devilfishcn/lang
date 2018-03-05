import tornado.gen
import tornado.web

import tornado.httpclient

import json

@tornado.gen.coroutine
def post(self):
    resp = yield GetUser()
    self.write(resp)

@tornado.gen.coroutine
def GetUser():
    client = tornado.httpclient.AsyncHTTPClient()
    resp = yield client.fetch("https://api.github.com/users")
    if resp.code == 200:
        resp = tornado.escape.json_decode(resp.body)
    else:
        resp = {"message": "fetch client error"}
        print("client fetch error %d, %s" % (resp.code, resp.message))
    raise tornado.gen.Return(resp)


m=post()
m.result()
