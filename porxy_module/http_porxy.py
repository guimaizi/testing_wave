# coding: utf-8
'''
    @Author guimaizi
    @Date 3/30/2020 14:00
    mitmdump -s ./http_porxy.py
    powsershell   .\chrome.exe  --proxy-server="127.0.0.1:8788"
'''
from mitmproxy import http
#from pymongo import MongoClient
import time,json,pymongo

class AddHeader(object):
    def __init__(self):
        client = pymongo.MongoClient(host='192.168.0.137',port=27017)
        self.db_target_domain = client['testing_wave']['main']
        #db_target_domain.authenticate(config_main.callback_mongo_config()['name'], config_main.callback_mongo_config()['password'])
        #self.collection = self.db_target_domain['data_table_%s'%time.strftime('%Y-%m-%d',time.localtime()).replace('-','_')]
        #self.collection = self.db_target_domain.main
    def filter_http(self,flow):
        #for i in flow.response.headers:
        #    print(i)
        if flow.response.status_code in [200,301,302,401] \
                and 'css' not in flow.response.headers["Content-Type"] \
                and 'image' not in flow.response.headers["Content-Type"] \
                and flow.request.method in ['GET','POST']:
            return True 
        return False
    def callback_json(self,headers):
        headers_arr={}
        for value in headers:
            if value !='Host':
                headers_arr["%s"%value]="%s"%headers[value]
        return headers_arr

    def response(self,flow):
        if self.filter_http(flow)!=False:
            if flow.request.method=='GET':method=0
            else:method=1
            if flow.request.get_text()!='':
                post=flow.request.get_text()
            else:post='null'
            data={"state":0,"url":'%s'%flow.request.url,
                  "headers":self.callback_json(flow.request.headers),"post":post,"method":method,"time":time.strftime('%Y-%m-%d',time.localtime())}
            #collection = self.db_target['data_list']
            self.db_target_domain.insert_one(data)
            print(data)




addons = [AddHeader()]