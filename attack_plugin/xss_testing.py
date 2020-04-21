# coding: utf-8
'''
Created on Nov 12, 2019

@author: guimaizi
'''
from config_module import param_process, http_testing, config_function


class xss_testing:
    def __init__(self):
        '''xss测试'''
        self.config= config_function.config_function()
        self.param_process= param_process.param_process(['\'"GuImAizI<GuImAizI>'])
        self.http_testing= http_testing.http_testing()
    def run(self):
        for target_list in self.param_process.main(self.config.callback_target()):
            for target in target_list:
                html_text=self.http_testing.callback_response(target['data'])
                if '"GuImAizI' in html_text or '<GuImAizI>' in html_text:
                    self.config.Generated_text('XSS: %s\n %s'%(target['name_param'],target['data']))
if __name__ == '__main__':
    p1=xss_testing()
    p1.run()