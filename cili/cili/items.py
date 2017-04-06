# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CiliItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    topic=scrapy.Field()
    magnet=scrapy.Field()
    ed2k=scrapy.Field()
    size=scrapy.Field()
    
