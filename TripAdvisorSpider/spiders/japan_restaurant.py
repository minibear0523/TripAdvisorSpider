# -*- coding: utf-8 -*-
import scrapy


class JapanRestaurantSpider(scrapy.Spider):
    name = "japan_restaurant"
    allowed_domains = ["tripadvisor.cn"]
    start_urls = (
        'http://www.tripadvisor.cn/',
    )

    def parse(self, response):
        pass
