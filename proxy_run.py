# coding: utf-8
'''
    @Author guimaizi
    @Date 5/1/2020 9:06
'''
# coding: utf-8
'''
    @Author guimaizi
    @Date 5/1/2020 9:05
'''
# coding: utf-8
'''
Created on Nov 25, 2019

@author: guimaizi
'''
from attack_plugin import xss_testing,sqlinj_testing,waf_test,cmd_inj
from config_module import filter_similarity,mongo_con,config_function
class proxy_run:
    def __init__(self):
        print('--------------------------\n\n')
        print('-------scaning...--------\n\n')
        print('--------------------------\n\n\n')
    def auto_porxy_run(self):
        '''
        : http请求代理数据库检测模式
        :return:
        '''
        try:
            mongo_cons=mongo_con.mongo_con()
            if mongo_cons.find_request_count()>=1:
                request_data=mongo_cons.callback_request()
                #print(request_data)
                xss=xss_testing.xss_testing()
                xss.reflected_run(request_data)
                sql_inj=sqlinj_testing.sqlinj_testing( )
                sql_inj.run(request_data)
                cmd_in=cmd_inj.cmd_inj()
                cmd_in.run(request_data)
        finally:
            mongo_cons.updete_request(request_data['_id'])
    def main(self):
        pass
if __name__ == '__main__':
    p1=proxy_run()
    p1.auto_porxy_run()