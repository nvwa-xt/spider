from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector

from wooyun.items import WooyunItem


class StackSpider(CrawlSpider):
    name = "wooyun"
    allowed_domains = ["wooyun.org"]
    start_urls = [
        "http://wooyun.org/bugs/new_public/page/1",]
    rules = (
        Rule(
            SgmlLinkExtractor(allow=('/bugs/new_public/page/\d+')),
            callback='parse_item',
            follow=True ), )

    def parse_item(self, response):
        hxs = Selector(response)
        sels = hxs.xpath('//div[@class="content"]/h3')
        for sel in sels:
            item = WooyunItem()
            item['title'] = sel.xpath(
                '//td/a/text()').extract()[0]
            item['url'] = sel.xpath(
                '//td/a/@href').extract()[0]
            yield item
