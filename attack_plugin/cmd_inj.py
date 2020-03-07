# coding: utf-8
'''
Created on Nov 12, 2019

@author: guimaizi
'''
import config_function,param_process,http_testing
class cmd_inj:
    def __init__(self):
        '''命令注入测试'''
        self.config=config_function.config_function()
        self.param_process=param_process.param_process(['aaa'])
        self.http_testing=http_testing.http_testing()
    def run(self):
        for target_list in self.param_process.main(self.config.callback_target()):
            for target in target_list:
                if 'aa ' in self.http_testing.callback_response(target['data']):
                    pass
if __name__ == '__main__':
    p1=cmd_inj()
    p1.run()