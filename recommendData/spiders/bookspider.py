# -*- coding: utf-8 -*-
import scrapy
import os
from scrapy.selector import Selector

from recommendData.items import BooksItem


class BookspiderSpider(scrapy.Spider):
    name = 'bookspider'
    allowed_domains = ['book.douban.com']
    start_urls = ['https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4',
                  'https://book.douban.com/tag/%E4%B8%AD%E5%9B%BD%E6%96%87%E5%AD%A6',
                  'https://book.douban.com/tag/%E5%8F%A4%E5%85%B8%E6%96%87%E5%AD%A6',
                  'https://book.douban.com/tag/%E5%AD%A6%E6%9C%AF',
                  'https://book.douban.com/tag/%E6%8E%A8%E7%90%86',
                  'https://book.douban.com/tag/%E7%BB%98%E6%9C%AC',
                  'https://book.douban.com/tag/%E7%A7%91%E5%B9%BB',
                  'https://book.douban.com/tag/%E9%87%91%E5%BA%B8',
                  'https://book.douban.com/tag/%E5%8E%86%E5%8F%B2',
                  'https://book.douban.com/tag/%E5%BF%83%E7%90%86%E5%AD%A6',
                  'https://book.douban.com/tag/%E4%BC%A0%E8%AE%B0',
                  'https://book.douban.com/tag/%E5%9B%9E%E5%BF%86%E5%BD%95',
                  'https://book.douban.com/tag/%E6%80%9D%E6%83%B3',
                  'https://book.douban.com/tag/%E7%88%B1%E6%83%85',
                  'https://book.douban.com/tag/%E6%88%90%E9%95%BF',
                  'https://book.douban.com/tag/%E7%94%9F%E6%B4%BB',
                  'https://book.douban.com/tag/%E6%97%85%E8%A1%8C',
                  'https://book.douban.com/tag/%E7%BB%8F%E6%B5%8E%E5%AD%A6',
                  'https://book.douban.com/tag/%E7%BB%8F%E6%B5%8E%E5%AD%A6',
                  'https://book.douban.com/tag/%E7%A7%91%E6%99%AE',
                  'https://book.douban.com/tag/%E7%BC%96%E7%A8%8B',
                  'https://book.douban.com/tag/%E7%A7%91%E5%AD%A6',
                  'https://book.douban.com/tag/%E7%A7%91%E6%8A%80',
                  'https://book.douban.com/tag/%E6%B8%B8%E8%AE%B0',
                  'https://book.douban.com/tag/%E7%BE%8E%E9%A3%9F',
                  'https://book.douban.com/tag/%E5%85%BB%E7%94%9F',
                  'https://book.douban.com/tag/%E5%88%9B%E4%B8%9A'
                  ]

    def parse(self, response):
        sel = Selector(response)
        book_list = sel.css('#subject_list >ul>li')
        book_type = sel.css('#content')
        count = 0  # 用于设置爬取的页数
        for book in book_list:
            item = BooksItem()
            try:
                item['book_type'] = book_type.xpath('h1/text()').extract()[0].strip()
                item['book_name'] = book.xpath('div[@class="info"]/h2/a/text()').extract()[0].strip()
                item['book_star'] = book.xpath("div[@class='info']/div[2]/span[@class='rating_nums']/text()").extract()[0].strip()
                pub = book.xpath('div[@class="info"]/div[@class="pub"]/text()').extract()[0].strip().split('/')
                item['book_price'] = pub.pop()
                item['book_date'] = pub.pop()
                item['book_publish'] = pub.pop()
                item['book_author'] = '/'.join(pub)
                item['book_img'] = book.xpath('div[@class="pic"]/a/img/@src').extract()[0].strip()
                item['book_content'] = book.xpath('div[@class="info"]/p/text()').extract()[0].strip()
                yield item
            except:
                pass
        nextPage = sel.xpath('//div[@id="subject_list"]/div[@class="paginator"]/span[@class="next"]/a/@href').extract()[0].strip()
        if nextPage:
            next_url = 'https://book.douban.com' + nextPage
            count += 1
            yield scrapy.http.Request(next_url, callback=self.parse)
        if count > 50:
            os.exit();
