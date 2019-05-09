# -*- coding: utf-8 -*-
from scrapy import Spider , Selector , Request 
from scrapy.spiders import CrawlSpider , Rule  
from ..items import ProxyItem 
from scrapy.linkextractors import LinkExtractor 

class KuaidailiSpider(CrawlSpider):
    name = 'kuaidaili'
    allowed_domains = ['kuaidaili.com']
    start_urls = ['https://www.kuaidaili.com/free/inha/1/']
    rules = (Rule(LinkExtractor(allow = ('/free/inha/*'),),follow=True ,callback = 'parse_items' ),)

    def parse_items (self, response):
        selector = Selector(response)
        row_selectors = selector.xpath("//tr")

        for row_selector in row_selectors :
            item = ProxyItem()
            
            # .extract() return a list , .extract_first() return the first element of the list , where there is only one element 
            # in this case 
            item['ip'] = row_selector.xpath("td[1]/text()").extract_first()
            item['port'] = row_selector.xpath("td[2]/text()").extract_first()
            item['protocol'] = row_selector.xpath("td[4]/text()").extract_first()
            item['location'] = row_selector.xpath("td[5]/text()").extract_first()
            # calling a method inside another method should use self. at the beginning 
            item['speed'] = self.duration_to_millisecond( row_selector.xpath("td[6]/text()").extract_first())
            item['validation_date'] = row_selector.xpath("td[7]/text()").extract_first()

            yield item 
    # the first parameter of a method should be self. 
    def duration_to_millisecond(self,val):

        if val:
            if u'秒' in val :
                return int(float(val.replace(u'秒',''))*1000)
            if u'分钟' in val :
                return int(float(val.replace(u'分钟',''))*1000*60)
            if u'小时' in val :
                return int(float(val.replace(u'小时',''))*1000*60*60)
        else:
            return 0 
