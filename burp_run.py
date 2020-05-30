# coding: utf-8
'''
Created on Nov 25, 2019

@author: guimaizi
'''
from attack_plugin import xss_testing,sqlinj_testing,waf_test,cmd_inj
from config_module import filter_similarity,mongo_con,config_function
class burp_run:
    def __init__(self):
        print('--------------------------\n\n')
        print('-------scaning...--------\n\n')
        print('--------------------------\n\n\n')
    def burp_test_run(self):
        '''
        : burp插件模式
        :return:
        '''
        try:
            config_=config_function.config_function()
            waf=waf_test.waf_test()
            if waf.run(config_.callback_target())!=0:
                cmd_in=cmd_inj.cmd_inj()
                cmd_in.run(config_.callback_target())
                sql_inj=sqlinj_testing.sqlinj_testing()
                sql_inj.run(config_.callback_target())
            xss=xss_testing.xss_testing()
            xss.reflected_run(config_.callback_target())
        except Exception as e:
            print(e)
        finally:
            filter=filter_similarity.filter_similarity()
            filter.run_filter(config_.callback_target())
            print('\n-------------\nfinished')
if __name__ == '__main__':
    p1=burp_run()
    p1.burp_test_run()
    #p1.auto_porxy_run()