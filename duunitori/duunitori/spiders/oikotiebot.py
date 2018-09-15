# -*- coding: utf-8 -*-
"""
Search Jobs from oikotie
"""
import scrapy
from scrapy.utils.project import get_project_settings
from duunitori.items import DuunitoriItem


# class Job(scrapy.Item):
#     """Represents Job object """
#     title = scrapy.Field()
#     company = scrapy.Field()
#     description = scrapy.Field()
#     link = scrapy.Field()

    

class MolbotSpider(scrapy.Spider):
    """
    Search jobs based on keywords and companies
    """
    name = 'oikotiebot'
    allowed_domains = ['oikotie.fi']
    start_urls = []
    settings = get_project_settings()
    keywords = settings.getlist('KEYWORDS')
    keywords = keywords + settings.getlist('COMPANIES')
    
    
    for key in keywords:
        start_urls.append('https://tyopaikat.oikotie.fi/haku?sijainti[101]=101&jq={}&sort_by=score&page=0'.format(key))
        
    def parse(self, response):
        jobs = response.css('ul.joblist').css('li')
        for job in jobs:
            
            _company = job.css('h6::text').extract()[0].split('|')[0].strip()
            item = DuunitoriItem(title = job.css('h4::text').extract(), description = "empty for now",company = _company ,  link= job.xpath('./a/@href').extract())
            yield item
            
            