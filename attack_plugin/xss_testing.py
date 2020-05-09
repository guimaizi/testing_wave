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
        self.payload=['\'"GuImAizI<GuImAizI>']
        self.param_process= param_process.param_process(self.payload)
        self.http_testing= http_testing.http_testing()
    def reflected_run(self,request_data):
        try:
            for target_list in self.param_process.main(request_data):
                for target in target_list:
                    html_text=self.http_testing.callback_response(target['data'])
                    if '"GuImAizI' in html_text or '<GuImAizI>' in html_text:
                        self.config.Generated_text('XSS: %s\n %s'%(target['name_param'],target['data']))
                request_data['url']=request_data['url']+self.payload[0]
                html_text=self.http_testing.callback_response(request_data)
                if '"GuImAizI' in html_text or '<GuImAizI>' in html_text:
                    self.config.Generated_text('XSS: %s\n '%(request_data['url']))
        except Exception as e:
            print(e)
if __name__ == '__main__':
    p1=xss_testing()
    p1.reflected_run()