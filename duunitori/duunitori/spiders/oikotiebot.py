# -*- coding: utf-8 -*-
"""
Search Jobs from oikotie
"""
import scrapy

class Job(scrapy.Item):
    """Represents Job object """
    title = scrapy.Field()
    company = scrapy.Field()
    description = scrapy.Field()
    link = scrapy.Field()

class MolbotSpider(scrapy.Spider):
    """
    Search jobs based on keywords and companies
    """
    name = 'oikotiebot'
    allowed_domains = ['oikotie.fi']
    start_urls = []
    key_words = ['python', '.net', 'labview', 'TestStand', 'C#', 'rust', 'embedded', 'iot', 'avr',  'amazon', 'azure', 'arm', 'elektroniikka', 'electronics',  'jtag', 'qt']
    companies = ['kavo kerr', 'suunto', 'metos', 'murata', 'thermo-fisher', 'vaisala', 'rocla', 'valmet', 'kone', 'Steris', 'etteplan']
    for key in key_words:
        start_urls.append('https://tyopaikat.oikotie.fi/haku?sijainti[101]=101&jq={}&sort_by=score&page=0'.format(key))

    for company in companies:
        start_urls.append('https://tyopaikat.oikotie.fi/haku?sijainti[101]=101&jq={}&sort_by=score&page=0'.format(company))
        
    def parse(self, response):
        jobs = response.css('ul.joblist').css('li')
        for job in jobs:
            item = Job(title = job.css('h4::text').extract(), description = "empty for now", company = job.css('h6 span span::text').extract(),  link= job.xpath('./a/@href').extract())
            yield item
            