# coding: utf-8
'''
    @Author guimaizi
    @Date 3/16/2020 10:49
'''
from config_module import config_function
from pymongo import MongoClient
class mongo_con:
    def __init__(self):
        '''
        : mongodb 操作
        '''
        self.config_main=config_function.config_function()
        self.client = MongoClient(self.config_main.callback_mongo_config()['ip'], self.config_main.callback_mongo_config()['port'])
        self.db_target = self.client.testing_wave
        if self.config_main.callback_mongo_config()['name']!='':
            self.db_target.authenticate(self.config_main.callback_mongo_config()['name'], self.config_main.callback_mongo_config()['password'])
    def find_param(self,url_api ):
        collection = self.db_target['filter_list']
        return collection.find({"url_api": "%s"%url_api}).count()
    def into_param(self,data):
        collection = self.db_target['filter_list']
        collection.insert_one(data)
    def callback_param_list(self,url_api):
        collection = self.db_target['filter_list']
        return collection.find({"url_api": "%s"%url_api})
    def update_param_list(self,url_api,url_param):
        collection = self.db_target['filter_list']
        collection.update_one({"url_api": url_api},{"$set": {"url_param_list": url_param}})
    def find_request_count(self):
        collection = self.db_target['request_http_list']
        return collection.find({"state": 0}).count()
    def callback_request(self):
        collection = self.db_target['request_http_list']
        data=collection.find({"state": 0}).limit(1)[0]
        return data
    def updete_request(self,_id):
        collection = self.db_target['request_http_list']
        collection.update_one({"_id": _id},{"$set": {"state": 1}})

if __name__ == '__main__':
    item=mongo_con()
    '''{"domain":"%s"%urlparse(data[0][0]['data']['url']).hostname,"url_api":"%s://%s%s"%(url_param.scheme,url_param.netloc,url_param.path),"url_param_list":[],"time":time.asctime(time.localtime(time.time())),"state_code":1}'''
    print(item.callback_request())