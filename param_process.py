# coding: utf-8
'''
Created on Nov 14, 2019

@author: guimaizi
'''
from urllib import parse
import config_function,copy,ast,json

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

    def json_process(self,param):
        try:
            list_data=[]
            #print(data)
            json_str = json.dumps(param, sort_keys=True)
            # 将 JSON 对象转换为 Python 字典
            params_json = json.loads(json_str)
            items = params_json.items()
            for key, value in items:
                if type(value)==type('str'):
                    copy_data=copy.deepcopy(param)
                    list_param_payload=[]
                    for payload in self.payload_list:
                        copy_data[key]=copy_data[key]+payload
                        list_param_payload.append({"name_param":"%s"%key,"param":copy_data})
                    list_data.append(list_param_payload)
            return list_data
        except Exception as e:
            print(e)
            return []
    def callback_json_param(self,data):
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
    payload_list=['XSSGUIMAIZI','SQLINJ']
    p1=param_process(payload_list)
    tmp1={'aaaa':'AASDSAdasdas',"cccc":"asdsadasdsa","dsadsa":1111,"sadasdas":"dsadasdsa"}
    print(p1.json_process(tmp1))