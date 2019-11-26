# coding: utf-8
'''
Created on Nov 14, 2019

@author: guimaizi
'''
from urllib import parse
import config_function,copy
class param_process:
    def __init__(self,payload_list):
        self.config=config_function.config_function()
        self.payload_list=payload_list
    def url_process(self,url):
        print(url)

    def param_process(self,param):
        try:
            num=0
            callback_param=[]
            for tmp in param.split('&'):
                param_tuple=[]
                for payload in self.payload_list:
                    tmp_param=param.split('&')
                    param_name=tmp_param[num].split('=')[0]
                    tmp_param[num]=tmp_param[num]+payload
                    param_tuple.append({"name_param":"%s"%param_name,"param":'&'.join(tmp_param)})
                callback_param.append(param_tuple)
                num=num+1
            return callback_param
        except Exception as e:
            print(e)
            return []

    def json_process(self):
        pass
    def callback_get_param(self,data):
        list_data=[]
        url_tmp=parse.urlparse(data['url'])
        if '=' in url_tmp.query:
            for param_list in self.param_process(url_tmp.query):
                list_param_payload=[]
                for param in param_list:
                    url=data['url']
                    url_frist=url.split('?')[0]
                    data['url']=url_frist+'?'+param['param']
                    real_data={"name_param":param['name_param'],"data":data}
                    copy_data=copy.deepcopy(real_data)
                    list_param_payload.append(copy_data)
                list_data.append(list_param_payload)
        return list_data
    def callback_post_param(self,data):
        list_data=[]
        for param_list in self.param_process(data['post']):
            list_param_payload=[]
            for param in param_list:
                data['post']=param['param']
                #print(data['post'])
                real_data={"name_param":param['name_param'],"data":data}
                copy_data=copy.deepcopy(real_data)
                list_param_payload.append(copy_data)
            list_data.append(list_param_payload)
        return list_data
    def main(self,data):
        list_data=[]
        copy_data=copy.deepcopy(data)
        if data['method']==1:
            url_tmp=parse.urlparse(data['url'])
            if '=' in url_tmp.query:
                list_data.extend(self.callback_get_param(data))
            list_data.extend(self.callback_post_param(copy_data))
        elif data['method']==0:
            list_data.extend(self.callback_get_param(data))
        return list_data
if __name__ == '__main__':
    p1=param_process()
    payload_list=['XSSGUIMAIZI','SQLINJ']
    for i in p1.main(payload_list):
        print(i)
        
    #param='dada=adada&dasda@d=1&fsdfs=111&23131=dasda&FDSF='
    #p1.param_process(param,payload_list)
    #print(p1.url_process(url, payload))