# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from logging import log

from scrapy.utils.project import get_project_settings
settings = get_project_settings()


class StockstarPipeline(object):
    # def __init__(self, mongo_url, mongo_db):
    #     #链接MongoDB
    #     self.mongo_url = mongo_url
    #     self.mongo_db = mongo_db
    #
    # @classmethod
    # def from_cralwer(cls, crawler):
    #     return cls(
    #         mongo_url = crawler.settings.get("MONGO_URL"),
    #         mongo_db = crawler.settings.get('MONGO_DB')
    #     )
    #
    # def open_spider(self, spider):
    #     self.client = pymongo.MongoClient(self.mongo_url)
    #     self.db = self.client[self.mongo_db]
    #
    # def process_item(self, item, spider):
    #     # name =item.__class__.__name__
    #     self.db['stock'].insert(dict(item))
    #     return item
    #
    # def close_spider(self, spider):
    #     self.client.close()



    # def __init__(self, databaseIp='127.0.0.1', databasePort=27017,mongodbName='stock'):
    #     client = pymongo.MongoClient(databaseIp, databasePort)
    #     self.db = client[mongodbName]
    #
    # def process_item(self, item, spider):
    #     postItem = dict(item)  # 把item转化成字典形式
    #     self.db.scrapy.insert(postItem)  # 向数据库插入一条记录
    #     return item  # 会在控制台输出原item数据，可以选择不写

    def __init__(self):
        # 链接数据库
        self.client = pymongo.MongoClient(host=settings['MONGO_HOST'], port=settings['MONGO_PORT'])
        # 数据库登录需要帐号密码的话
        # self.client.admin.authenticate(settings['MINGO_USER'], settings['MONGO_PSW'])
        self.db = self.client[settings['MONGO_DB']]  # 获得数据库的句柄
        self.coll = self.db[settings['MONGO_COLL']]  # 获得collection的句柄

    def process_item(self, item, spider):
        postItem = dict(item)  # 把item转化成字典形式
        self.coll.insert(postItem)  # 向数据库插入一条记录
        #return item  # 会在控制台输出原item数据，可以选择不写

