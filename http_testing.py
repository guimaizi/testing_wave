# coding: utf-8
'''
Created on Nov 12, 2019

@author: guimaizi
'''
import config_function,requests,json
class http_testing:
    def __init__(self):
        '''http/s重放发包'''
        self.config_param=config_function.config_function()
    def http_get(self,data):
        try:
            r=requests.get(data['url'],headers=data['headers'],timeout=self.config_param.time_out)
            r.close()
            return r.text
        except:return 'null'
    def http_post(self,data):
        try:
            proxies = { "http": "http://127.0.0.1:8080"}
            if type(data['post'])==type({'a':1}):
                r=requests.post(data['url'],data=json.dumps(data['post']),proxies=proxies,headers=data['headers'],timeout=self.config_param.time_out)
            else:
                r=requests.post(data['url'],data=str(data['post']),proxies=proxies,headers=data['headers'],timeout=self.config_param.time_out)
            r.close()
            #print(r.text)
            return r.text
        except:return 'null'
    def callback_response(self,data):
        if data['method']==1:
            return self.http_post(data)
        else:return self.http_get(data)