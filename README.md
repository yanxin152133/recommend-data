# recommend-data
爬取豆瓣读书书籍信息

## 入库
编辑**pipelines.py**文件：
           
```html
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql as db


class RecommenddataPipeline(object):
    def __init__(self):
        self.con = db.connect(user="root", passwd="123456+", host="localhost",
                              db="recommend", charset="utf8")
        self.cur = self.con.cursor()

    def process_item(self, item, spider):
        book_name = item.get("book_name", "N/A")  # 有的图书有数据项缺失，这里做了容错处理
        book_author = item.get("book_author", "N/A")
        book_publish = item.get("book_publish", "N/A")
        book_date = item.get("book_date", "N/A")
        book_price = item.get("book_price", "N/A")
        book_star = item.get("book_star", "N/A")
        book_img = item.get("book_img", "N/A")
        book_content = item.get("book_content", "N/A")
        book_type = item.get("book_type", "N/A")

        self.cur.execute(
            "insert into douban_books(id,book_name,book_author,book_publish,book_date,book_price,book_star,book_img,book_content,book_type) values(NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (item['book_name'], item['book_author'], item['book_publish'], item['book_date'], item['book_price'],
             item['book_star'], item['book_img'], item['book_content'], item['book_type']))
        self.con.commit()
        return item

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()

```

## 测试
```html
cd recommendData
scrapy crawl bookspider -o items.json  ## 将爬取的数据写入items.json文件中
```

## 运行
```html
scrapy crawl bookspider
```