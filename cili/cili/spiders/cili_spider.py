# -*- coding: utf-8 -*-
# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import scrapy
from scrapy.http import Request

from cili.items import CiliItem

class cilispider(scrapy.spiders.Spider):
    name="cili"     # 运行时这个爬虫的名字
    #start_urls=["http://oabt01.com/?_=25426"]
    start_urls=["http://oabt01.com/?topic_title3=%E7%A5%9E%E7%9B%BE%E5%B1%80%E7%89%B9%E5%B7%A5"]


    def parse(self,response):
        '''filename="oabt01today.txt"
        with open(filename,'wb') as f:
            f.write(response.body)
        
        for sel in response.xpath('//dl [@class="list-item"]'):
            topic=sel.xpath('dd/span[@class="b"]/a/text()').extract()
            magnet=sel.xpath('dd/@magnet').extract()
            ed2k=sel.xpath('dd/@ed2k').extract()
            size=sel.xpath('dd/span[@class="d"]/a/text()').extract()
            print magnet
        '''
        for sel in response.xpath('//dl [@class="list-item"]/dd'):
            item=CiliItem()
            item['topic']=sel.xpath('span[@class="b"]/a/text()').extract()
            item['magnet']=sel.xpath('@magnet').extract()
            item['ed2k']=sel.xpath('@ed2k').extract()
            item['size']=sel.xpath('span[@class="d"]/b/text()').extract()
            yield item      #提交经解析处理好的数据
            #print topic,magnet,ed2k,size

            
            #用Xpath语法指向除本页以外的所有页面链接
        for sel in response.xpath('//div[@class="pages"]/a[position()>1]'):
            urls=sel.xpath('@href').extract()
            url="http://oabt01.com"+urls[0]
            
            #将新获取的request返回给引擎，实现继续循环。也就实现了“自动下一网页的爬取”
            yield Request(url,callback=self.parse)
