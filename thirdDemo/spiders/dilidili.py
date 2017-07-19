# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from thirdDemo.items import ThirddemoItem
import time

class DilidiliSpider(scrapy.Spider):
    name = 'dilidili'
    allowed_domains = ['dilidili.wang']
    start_urls = ['http://dilidili.wang/hougong']

    def parse(self, response):
        url='http://www.dilidili.wang/hougong/'
        yield Request(url=url, callback=self.index1, dont_filter=True)

    def index1(self, response):
        url=response.xpath("//div[@class='con24 m-20 clear']//div[@class='nianfan']/a/@href").extract()
        #print(url)
        for i in range(len(url)):
            if url[i][-5:-3] == '20':
                yield Request(url=url[i], callback=self.next, dont_filter=True)

    def next(self,response):
        page_title_list=response.xpath("//div[@class='container clear']//div[@class='anime_list']//dt/a/@hrel").extract()
        #print(page_title_list)
        for i in range(len(page_title_list)):
            url="http://www.dilidili.wang"+page_title_list[i]
            #print(url)
            yield Request(url=url, callback=self.next2, dont_filter=True)


    def next2(self,response):

        page_title_list=response.xpath("//dt/img/@src").extract()   #//div[@class='aside_cen2']/div[@class='detail con24 clear']/dl
        page_title_country=response.xpath("//dd//div[@class='d_label']/a/text()").extract()
        page_title_title=response.xpath("//dd/h1/text()").extract()
        page_title_message=response.xpath("//dd//div[@class='d_label2']//text()").extract()
        page_title_message2 = response.xpath("//dd//div[@class='d_label']//text()").extract()
        #print(page_title_list )
        #print(page_title_country)
        #print(page_title_message)
        #print(page_title_message2)
        #try:
        #    print(page_title_country[0])
        #    print(page_title_list[0])
        #    print(page_title_title[0] )
        #    print(page_title_message2[2]+page_title_message2[3])
        #   print(page_title_message2[4]+page_title_message2[5])
        #    print(page_title_message[0]+page_title_message[1]+page_title_message[2]+page_title_message[3])
       # except:
        #    pass
        try:
            if page_title_country[0]=='日本':
                #print("123")
                item = ThirddemoItem()
                item['url']=page_title_list[0]
                item['title']=page_title_title[0]
                #item['message']=page_title_message2[2]+page_title_message2[3]+page_title_message2[4]+page_title_message2[5]+\
                 #            +page_title_message[0]+page_title_message[1]+page_title_message[2]+page_title_message[3]
                item['message']=page_title_message2[2]+page_title_message2[3]+page_title_message2[4]+page_title_message2[5]+page_title_message[0]+page_title_message[1]+page_title_message[2]+page_title_message[3]
                yield item
                #return item
                #print(item)
        except:
            pass
