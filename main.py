# coding: utf-8
'''
Created on Nov 25, 2019

@author: guimaizi
'''
from attack_plugin import xss_testing,sqlinj_testing,waf_test,cmd_inj
from config_module import filter_similarity
class main:
    def __init__(self):
        print('--------------------------\n\n')
        print('-------scaning...--------\n\n')
        print('--------------------------\n\n\n')
    def main(self):
        try:
            waf=waf_test.waf_test()
            if waf.run()!=0:
                cmd_in=cmd_inj.cmd_inj()
                cmd_in.run()
                sql_inj=sqlinj_testing.sqlinj_testing()
                sql_inj.run()
            xss=xss_testing.xss_testing()
            xss.run()
        except Exception as e:
            print(e)
        finally:
            filter=filter_similarity.filter_similarity()
            filter.run_filter()
            print('\n-------------\nfinished')
if __name__ == '__main__':
    p1=main()
    p1.main()