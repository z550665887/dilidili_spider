# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re
import urllib.request
import os


class ThirddemoPipeline(object):
    def process_item(self, item, spider):
        os.mkdir(r'D:/动漫收藏/'+item['title'])
        print(item['title'] + 'first build')
        file='D:/动漫收藏/'+item['title']+'/'+item['title']+'.jpg'
        print('Downloading:', file)
        urllib.request.urlretrieve(item['url'], filename=file)
        print('Finall:', file)
        file2= open('D:/动漫收藏/'+item['title']+'/'+'message.txt', 'w')
        file2.write(item['message'])
        file2.close()
