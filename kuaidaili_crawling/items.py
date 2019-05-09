# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class ProxyItem(Item):
    ip = Field()
    port = Field()
    protocol = Field() 
    location = Field()
    speed = Field()
    validation_date = Field() 
