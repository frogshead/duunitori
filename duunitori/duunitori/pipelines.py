# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3
import logging
from scrapy.exceptions import DropItem




class DuunitoriPipeline(object):
    """Remove empty items"""
    def process_item(self, item, spider):
        if item['link']:
            return item
        else:
            raise DropItem("Missing Link")


class DatabasePipeline(object):
    """Save items to database"""
    def __init__(self):
        self.client = sqlite3.connect("duunitori.db")
        self.cursor = self.client.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS duunit(id INTEGER PRIMARY KEY, url VARCHAR(255),title VARCHAR(255),company VARCHAR(255),description VARCHAR(255), row_added TEXT)")
    
    def process_item(self, item, spider):
        self.cursor.execute("SELECT * FROM duunit where url=?", item['link'])
        result = self.cursor.fetchone()
        if result:
            logging.debug("Item already database")
        else:
            self.cursor.execute("INSERT INTO duunit(url, title, company, description, row_added) VALUES(?, ?, ?, ?, datetime('now'))", (item['link'][0], item['title'][0], item['company'], item['description'][0],))
            self.client.commit()
            return item

    def close_spider(self, spider):
        """Close database connection"""
        self.client.close()
