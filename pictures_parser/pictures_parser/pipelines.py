# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class PicturesParserPipeline:
    # def get_media_requests(self, item, info):
    #     for image_url in item['image_url']:
    #         yield scrapy.Request(image_url)

    # def item_completed(self, results, item, info):
    #     image_paths = [x['path'] for ok, x in results if ok]
    #     if not image_paths:
    #         raise DropItem("Item contains no images")
    #     return item

    def process_item(self, item, spider):
        return item
