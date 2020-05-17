# coding: utf-8
'''
Created on Nov 14, 2019

@author: guimaizi
'''
from urllib import parse
import copy,time
from urllib.parse import urlparse
from config_module import config_function,filter_similarity


class param_process:
    def __init__(self,payload_list):
        '''
        : http请求包处理
        '''
        self.config= config_function.config_function()
        self.filter=filter_similarity.filter_similarity()
        self.payload_list=payload_list
    def callback_json_process(self,items,value):
        list_param_payload=[]
        for payload in self.payload_list:
            copy_data=copy.deepcopy(items)
            copy_data[value]=str(copy_data[value])+payload
            list_param_payload.append(copy_data)
        return list_param_payload
    def json_process(self,param):
        '''
        : {'a':1,'b':'str',c:{'a':1}}   json参数处理
        :param param:
        :return:
        '''
        try:
            list_data=[]
            items=eval(param)
            for value in items:
                if type(items[value])==type('str') or type(items[value])==type(1):
                    list_data.append({"name_param":"%s"%value,"data":self.callback_json_process(items, value)})
                elif type(items[value])==type({'aaa':'aaaa'}):
                    for itmes_param in items[value]:
                        list_data_first=[]
                        for data in self.callback_json_process(items[value],itmes_param):
                            copy_data=copy.deepcopy(items)
                            copy_data[value]=data
                            list_data_first.append(copy_data)
                        list_data.append({"name_param":"%s.%s"%(value,itmes_param),"data":list_data_first})
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
        '''
        : a=str&b=str&c=1  这类参数处理
        :param param:
        :return:
        '''
        try:
            num=0
            callback_param=[]
            for tmp in param.split('&'):
                param_tuple=[]
                for payload in self.payload_list:
                    tmp_param=param.split('&')
                    param_name=tmp_param[num].split('=')[0]
                    tmp_param[num]=tmp_param[num]+payload
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
                    url=data['url']
                    url_frist=url.split('?')[0]
                    data['url']=url_frist+'?'+param['param']
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
                real_data={"name_param":param_list['name_param'],"data":data}
                copy_data=copy.deepcopy(real_data)
                list_param_payload.append(copy_data)
            list_data.append(list_param_payload)
        return list_data
    def main(self,data):
        list_data=[]
        copy_data=copy.deepcopy(data)
        if data['method']==1:
            url_tmp=parse.urlparse(copy_data['url'])
            if '=' in url_tmp.query:
                list_data.extend(self.callback_get_param(copy_data))
            try:
                eval(copy_data['post'])
                list_data.extend(self.callback_json_param(copy_data))
            except:
                #print(self.callback_post_param(copy_data))
                list_data.extend(self.callback_post_param(copy_data))
        elif data['method']==0:
            if '?'  in copy_data['url'] and '='  in copy_data['url']:
                list_data.extend(self.callback_get_param(copy_data))
            elif self.filter.null_param_filter(self.config.callback_url_header(copy_data['url']))<1:
                list_data.extend(copy_data)
            else:list_data.extend([])
        if list_data!=[]:
            return self.filter.filter_param(list_data)
        else:return []
if __name__ == '__main__':
    payload_list=['XSSGUIMAIZI','SQLINJ']
    p1=param_process(payload_list)
    #tmp1={'aaaa':'AASDSAdasdas',"cccc":"asdsadasdsa","dsadsa":1111,"sadasdas":"dsadasdsa"}
    #print(p1.json_process(tmp1))
    tmp='tmp=aaaa&tmp1=bbbb&tmp2=ccccc'
    print(p1.param_process(tmp))
    for tmp in p1.param_process(tmp):
        print(tmp)