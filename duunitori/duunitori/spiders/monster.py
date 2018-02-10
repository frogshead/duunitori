# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.utils.project import get_project_settings

class Job(scrapy.Item):
    """Represents Job object """
    title = scrapy.Field()
    company = scrapy.Field()
    description = scrapy.Field()
    link = scrapy.Field()



class MonsterSpider(CrawlSpider):
    name = 'monster'
    settings = get_project_settings()
    keywords = settings.getlist('KEYWORDS')
    keywords = keywords + settings.getlist('COMPANIES')
    allowed_domains = ['monster.fi']
    start_urls = []

    # rules = (
    #     Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    # )

    for key in keywords:
        start_urls.append('https://www.monster.fi/tyopaikat/haku/?q={}&where=Alue__3AUusimaa&cy=fi'.format(key))

    def parse(self, response):
        
        jobs = response.xpath('//article')
        for job in jobs:
            print(job)
            item = Job(title = 'title')
            yield item
        
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        #yield item
