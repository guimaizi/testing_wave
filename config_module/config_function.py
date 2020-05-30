# coding: utf-8
'''
Created on Nov 12, 2019

@author: guimaizi
'''

import json
from config_module import mongo_con
from urllib.parse import urlparse

class config_function:
    def __init__(self):
        self.main_path='G:/Code/testing_wave/'
        with open('%s/config_module/config.json'%self.main_path,'r') as load_f:
            self.load_dict = json.load(load_f)
    def callback_target(self):
        '''
        : 返回测试目标
        :return:
        '''
        with open('%s/tmp/burp_tmp.json'%self.main_path, 'r') as f:
            data = json.load(f)
        return data
    def callback_burp_request(self):
        '''
        : 返回burp保存结果
        :return:
        '''
        with open('%s/tmp/burp_tmp.json'%self.callback_path(), 'r') as f:
            data = json.load(f)
        return data
    def callback_proxy_request(self):
        '''
            : 返回mongodb保存结果
            :return:
        '''
        mongo_cons=mongo_con.mongo_con()
        if mongo_cons.find_request_count()>1:
            print(mongo_cons.callback_request())
            #data=mongo_cons.callback_request()
            mongo_cons.updete_request(mongo_cons.callback_request())
    def callback_path(self):
        return self.load_dict['path']
    def callback_mongo_config(self):
        return self.load_dict['mongo_config']
    def callback_timeout(self):
        return self.load_dict['timeout']
    def Generated_text(self,data):
        '''
        :保存扫描器结果
        :param data:
        :return:
        '''
        print(data)
        file_result=open('%s/tmp/result.txt'%self.main_path,'a')
        file_result.write(data+'\n')
        file_result.close()
    def callback_url_header(self,url):
        url_param=urlparse(url)
        return "%s://%s%s"%(url_param.scheme,url_param.netloc,url_param.path)
if __name__ == '__main__':
    url='http://www.target.cn/zxft/20483.htm?dsdsa=dsadsa&dada=1&dsdada=3fdsf'
    payload='xsssguimaizi'
    p1=config_function()
    #print(p1.url_process(url, payload))
    print(p1.callback_burp_request())