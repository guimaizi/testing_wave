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
            waf=waf_test.waf_test()
            while 1:
                try:
                    request_data=mongo_cons.callback_request()
                    if mongo_cons.find_request_count()>=1:
                        if waf.run(mongo_cons.callback_request())!=0:
                            sql_inj=sqlinj_testing.sqlinj_testing()
                            sql_inj.run(mongo_cons.callback_request())
                            cmd_in=cmd_inj.cmd_inj()
                            cmd_in.run(mongo_cons.callback_request())
                        xss=xss_testing.xss_testing()
                        xss.reflected_run(mongo_cons.callback_request())
                        filter=filter_similarity.filter_similarity()
                        filter.run_filter(mongo_cons.callback_request())
                    else:return 0
                finally:
                    mongo_cons.updete_request(request_data['_id'])
        except Exception as e:
            print(e)
        finally:
            print('\n-------------\nfinished')
    def main(self):
        pass
if __name__ == '__main__':
    p1=proxy_run()
    p1.auto_porxy_run()