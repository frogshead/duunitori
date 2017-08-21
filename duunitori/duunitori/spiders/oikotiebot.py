# -*- coding: utf-8 -*-
import scrapy

class Job(scrapy.Item):
    """Represents Job object """
    title = scrapy.Field()
    company = scrapy.Field()
    description = scrapy.Field()
    link = scrapy.Field()

class MolbotSpider(scrapy.Spider):
    name = 'oikotiebot'
    allowed_domains = ['oikotie.fi']
    base_url = 'https://tyopaikat.oikotie.fi/haku?sijainti[101]=101&jq=python&sort_by=score&page=0'
    start_urls = []
    key_words = ['python', '.net', 'labview', 'TestStand', 'C#', 'embedded', 'iot', 'avr' 'amazon', 'azure']
    companies = ['kavo-kerr', 'suunto', 'metos', 'murata', 'thermo-fisher', 'vaisala']
    for key in key_words:
        start_urls.append('https://tyopaikat.oikotie.fi/haku?sijainti[101]=101&jq={}&sort_by=score&page=0'.format(key))

    for company in companies:
        start_urls.append('https://tyopaikat.oikotie.fi/haku?sijainti[101]=101&jq={}&sort_by=score&page=0'.format(company))
        
    def parse(self, response):
        jobs = response.css('ul.joblist').css('li')
        for job in jobs:
            item = Job(title = job.css('h4::text').extract(), description = "empty for now", company = job.css('h6 span span::text').extract(),  link= job.xpath('./a/@href').extract())
            yield item
            