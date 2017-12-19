# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import pymongo
from scrapy.conf import settings
from scrapy.exceptions import DropItem
from scrapy import log

class MongoDBPipeline(object):
    def open_spider(self, spider):
        self.connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        self.db = self.connection[settings['MONGODB_DB']]
        self.collection = self.db[settings['MONGODB_COLLECTION']]

        log.msg('Load nid from MongoDB database!',
                level=log.DEBUG, spider=spider)
        self.itemlist = set()
        for i in self.collection.find():
            self.itemlist.add(i['id'])

    def close_spider(self, spider):
        self.connection.close()

    def process_item(self, item, spider):
        if item['id'] in self.itemlist:
            raise DropItem('Duplication data!')
        #self.collection.update({'nid': item['nid']}, dict(item), upsert=True)
        self.collection.insert(dict(item))
        log.msg('Goods added to MongoDB database!',
                level=log.DEBUG, spider=spider)
        return item
