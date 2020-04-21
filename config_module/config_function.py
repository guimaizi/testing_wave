# coding: utf-8
'''
Created on Nov 12, 2019

@author: guimaizi
'''

import json
class config_function:
    def __init__(self):
        main_path='G:/Code/testing_wave/config_module/config.json'
        with open(main_path,'r') as load_f:
            self.load_dict = json.load(load_f)
        self.time_out=10
    def callback_target(self):
        '''
        : 返回burp保存结果
        :return:
        '''
        with open('G:/Code/testing_wave/tmp/burp_tmp.json', 'r') as f:
            data = json.load(f)
        return data
    def callback_burp_request(self):
        '''
        : 返回burp保存结果
        :return:
        '''
        with open('G:/Code/testing_wave/tmp/burp_tmp.json', 'r') as f:
            data = json.load(f)
        return data
    def callback_mongo_config(self):
        return self.load_dict['mongo_config']
    def Generated_text(self,data):
        '''
        :保存扫描器结果
        :param data:
        :return:
        '''
        print(data)
    def into_param_list(self):
        pass
if __name__ == '__main__':
    url='http://www.target.cn/zxft/20483.htm?dsdsa=dsadsa&dada=1&dsdada=3fdsf'
    payload='xsssguimaizi'
    p1=config_function()
    #print(p1.url_process(url, payload))
    print(p1.callback_burp_request())