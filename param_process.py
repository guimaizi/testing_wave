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
    def json_process(self,param):
        try:
            list_data=[]
            items=eval(param)
            for value in items:
                list_param_payload=[]
                if type(items[value])==type('str') or type(items[value])==type(1):
                    for payload in self.payload_list:
                        copy_data=copy.deepcopy(items)
                        copy_data[value]=str(copy_data[value])+payload
                        list_param_payload.append(copy_data)
                    list_data.append({"name_param":"%s"%value,"data":list_param_payload})
            return list_data
        except Exception as e:
            print(e)
            return []
    def callback_json_param(self,data):
        list_data=[]
        for param_list in self.json_process(data['post']):
            #print(param_list)
            list_param_payload=[]
            for param in param_list['data']:
                #print(param)
                data['post']=param
                real_data={"name_param":param_list['name_param'],"data":data}
                copy_data=copy.deepcopy(real_data)
                list_param_payload.append(copy_data)
            list_data.append(list_param_payload)
        return list_data
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
                    #param_tuple.append({"name_param":"%s"%param_name,"param":'&'.join(tmp_param)})
                    param_tuple.append({"param":'&'.join(tmp_param)})
                param_tmp={"name_param":"%s"%param_name,"data":param_tuple}
                callback_param.append(param_tmp)
                num=num+1
            return callback_param
        except Exception as e:
            print(e)
            return []
    def callback_get_param(self,data):
        list_data=[]
        url_tmp=parse.urlparse(data['url'])
        if '=' in url_tmp.query:
            for param_list in self.param_process(url_tmp.query):
                list_param_payload=[]
                for param in param_list['data']:
                    #print(param)
                    url=data['url']
                    url_frist=url.split('?')[0]
                    data['url']=url_frist+'?'+param['param']
                    #print(data['url'])
                    real_data={"name_param":param_list['name_param'],"data":data}
                    copy_data=copy.deepcopy(real_data)
                    list_param_payload.append(copy_data)
                list_data.append(list_param_payload)
        return list_data
    def callback_post_param(self,data):
        list_data=[]
        for param_list in self.param_process(data['post']):
            list_param_payload=[]
            for param in param_list['data']:
                data['post']=param['param']
                #print(data['post'])
                real_data={"name_param":param_list['name_param'],"data":data}
                copy_data=copy.deepcopy(real_data)
                list_param_payload.append(copy_data)
            list_data.append(list_param_payload)
        return list_data
    def main(self,data):
        '''result:
        ###常规参数：
        [{'name_param': 'tmp', 'data': [
        {'param': 'tmp=aaaaXSSGUIMAIZI&tmp1=bbbb&tmp2=ccccc'}, 
        {'param': 'tmp=aaaaSQLINJ&tmp1=bbbb&tmp2=ccccc'}]},
         {'name_param': 'tmp1', 'data': [
         {'param': 'tmp=aaaa&tmp1=bbbbXSSGUIMAIZI&tmp2=ccccc'},
          {'param': 'tmp=aaaa&tmp1=bbbbSQLINJ&tmp2=ccccc'}]},
           {'name_param': 'tmp2', 'data': [
           {'param': 'tmp=aaaa&tmp1=bbbb&tmp2=cccccXSSGUIMAIZI'}, 
           {'param': 'tmp=aaaa&tmp1=bbbb&tmp2=cccccSQLINJ'}]}]
        '''
        list_data=[]
        copy_data=copy.deepcopy(data)
        if data['method']==1:
            url_tmp=parse.urlparse(data['url'])
            if '=' in url_tmp.query:
                list_data.extend(self.callback_get_param(data))
            try:
                #print(copy_data)
                eval(copy_data['post'])
                list_data.extend(self.callback_json_param(copy_data))
            except:
                list_data.extend(self.callback_post_param(copy_data))
        elif data['method']==0:
            list_data.extend(self.callback_get_param(data))
        return list_data
if __name__ == '__main__':
    payload_list=['XSSGUIMAIZI','SQLINJ']
    p1=param_process(payload_list)
    #tmp1={'aaaa':'AASDSAdasdas',"cccc":"asdsadasdsa","dsadsa":1111,"sadasdas":"dsadasdsa"}
    #print(p1.json_process(tmp1))
    tmp='tmp=aaaa&tmp1=bbbb&tmp2=ccccc'
    print(p1.param_process(tmp))
    for tmp in p1.param_process(tmp):
        print(tmp)