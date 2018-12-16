# -*- coding: utf-8 -*-
import scrapy
import re


class StocksSpider(scrapy.Spider):
    name = 'stocks'
    #allowed_domains = ['baidu.com']
    start_urls = ['http://quote.eastmoney.com/stocklist.html']

    def parse(self, response):
        for href in response.css('a::attr(
