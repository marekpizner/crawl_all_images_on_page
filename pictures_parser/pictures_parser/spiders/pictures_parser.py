import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from ..items import PicturesParserItem

class PictureSpider(CrawlSpider):
    name = "picturespider"
    allowed_domains = ['domain.ca']

    start_urls = ['https://www.domain.ca']
    rules = [Rule(LinkExtractor(),
                  callback='parse', follow=False)]

    def parse(self, response):
        
        content = Selector(response=response).xpath('//body')
        for nodes in content:
            # build absolute URLs
            img_urls = ["https://www.domain.ca" + src for src in nodes.xpath('//img/@src').extract()]

            item = PicturesParserItem()
            item['page_heading'] = nodes.xpath("//title/text()").extract()
            item["page_title"] = nodes.xpath("//h1/text()").extract()
            item["page_link"] = response.url
            item["page_content"] = nodes.xpath('//div[@class="CategoryDescription"]').extract()

            item['image_urls'] = img_urls 
            # print(item)            
            yield item
