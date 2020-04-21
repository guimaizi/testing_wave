# coding: utf-8
'''
    @Author guimaizi
    @Date 3/27/2020 12:07
'''
from config_module import param_process, config_function,mongo_con
from urllib.parse import urlparse
import time
class filter_similarity:
    def __init__(self):
        '''
        : 去重
        '''
        self.config= config_function.config_function()
        self.mongo_con=mongo_con.mongo_con()
    def filter_param(self,data):
        '''
        : 过滤数据库重复参数
        :return:
        '''
        url_param=urlparse(data[0][0]['data']['url'])
        url_api="%s://%s%s"%(url_param.scheme,url_param.netloc,url_param.path)
        if self.mongo_con.find_param(url_api)==0:return data
        is_true=list(self.mongo_con.callback_param_list(url_api)[0]['url_param_list'])
        callback_data=[]
        #print(is_true)
        #url_param=urlparse(data[0][0]['data']['url'])
        for tmp in data:
            if tmp[0]['name_param'] not in is_true:
                callback_data.append(tmp)
        #print(callback_data)
        return callback_data
    def run_filter(self):
        '''
        : 去重 写入/更新数据库
        :return:
        '''
        param_fun= param_process.param_process(['a'])
        data=param_fun.main(self.config.callback_target())
        if len(data)==0:return 0
        url_param=urlparse(data[0][0]['data']['url'])
        url_api="%s://%s%s"%(url_param.scheme,url_param.netloc,url_param.path)
        if self.mongo_con.find_param(url_api)>0:
            url_param_list=list(self.mongo_con.callback_param_list(url_api)[0]['url_param_list'])
            for param in data:
                url_param_list.append(param[0]['name_param'])
            if list(set(url_param_list))!=url_param_list:
                self.mongo_con.update_param_list(url_api,list(set(url_param_list)))
        else:
            #[target_list[0]['name_param'] for target_list in data]
            self.mongo_con.into_param({"domain":"%s"%urlparse(data[0][0]['data']['url']).hostname,"url_api":url_api,"url_param_list":[target_list[0]['name_param'] for target_list in data],"time":time.asctime(time.localtime(time.time())),"state_code":1})
if __name__ == '__main__':
    p1=filter_similarity()
    p1.run_filter()