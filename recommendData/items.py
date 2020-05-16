# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BooksItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    book_name = scrapy.Field()  # 图书名v
    book_author = scrapy.Field()  # 图书作者v
    book_publish = scrapy.Field()  # 出版社v
    book_date = scrapy.Field()  # 出版日期v
    book_price = scrapy.Field()  # 图书价格v
    book_star = scrapy.Field()  # 图书评分v
    book_img = scrapy.Field()  # 封面
    book_content = scrapy.Field()  # 简介
    book_type = scrapy.Field()  # 类别
