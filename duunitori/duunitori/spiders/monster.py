# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.utils.project import get_project_settings
from scrapy.loader import ItemLoader
from duunitori.items import DuunitoriItem

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
        jobs = response.xpath('//section')
        print("Found {} jobs".format(len(jobs)))
        for job in jobs:
            item = DuunitoriItem()
            item['link'] = job.xpath('.//div/div/header/h2/a/@href').extract()
            item['company'] =  job.xpath('.//div/div/div/a/text()').extract()
            item['description'] = job.xpath('.//div/div/header/h2/a/text()').extract()
            item['title'] = job.xpath('.//div/div/header/h2/a/text()').extract()
            yield item