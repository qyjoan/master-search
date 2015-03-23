from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from capone.items import CaponeItem

class CapOneSpider(CrawlSpider):
    name = "capitalone"
    allowed_domains = ["capitalone.ca"]
    start_urls = ['https://www.capitalone.ca/']

    rules = (Rule(SgmlLinkExtractor(), callback='parse_url', follow=False), )

    def parse_url(self, response):
        item = CaponeItem()
        item['url'] = response.url
        return item
