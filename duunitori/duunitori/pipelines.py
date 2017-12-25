# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
import logging

class DuunitoriPipeline(object):
    def process_item(self, item, spider):
        if item['link']:
            return item
        else:
            raise DropItem("Missing Link")
