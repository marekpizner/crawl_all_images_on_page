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
                  callback='parse_url', follow=False)]

    def parse_url(self, response):
        
        content = Selector(response=response).xpath('//body')
        for nodes in content:

            # build absolute URLs
            img_urls = [urlparse.urljoin(response.url, src)
                        for src in nodes.xpath('//img/@src').extract()]

            item = HealthycommItem()
            item['page_heading'] = nodes.xpath("//title").extract()
            item["page_title"] = nodes.xpath("//h1/text()").extract()
            item["page_link"] = response.url
            item["page_content"] = nodes.xpath('//div[@class="CategoryDescription"]').extract()

            # use "image_urls" instead of "image_url"
            item['image_urls'] = img_urls 

            yield item
