# -*- coding: utf-8 -*-
import scrapy
from Baidu.items import BaiduItem

class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['tieba.baidu.com']
    start_urls = ['https://tieba.baidu.com/f?kw=%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB&ie=utf-8']

    def parse(self, response):
        postings = response.xpath('//div[@class="t_con cleafix"]')
        for posting in postings:
            item = BaiduItem()
            item['title'] = posting.xpath('.//a[@class="j_th_tit "]/text()').extract_first()
            item['author'] = posting.xpath('.//a[@class="frs-author-name j_user_card "]/text()').extract_first()
            item['reply'] = posting.xpath('.//span[@class="threadlist_rep_num center_text"]/text()').extract_first()
            yield item
