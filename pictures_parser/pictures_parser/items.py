# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PicturesParserItem(scrapy.Item):
    page_heading = scrapy.Field()
    page_title = scrapy.Field()
    page_link = scrapy.Field()
    page_content = scrapy.Field()
    page_content_block = scrapy.Field()

    image_url = scrapy.Field()
    image = scrapy.Field()
