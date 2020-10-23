# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class MoponCrawlerItem(scrapy.Item):
    name = scrapy.Field()
    discount_value = scrapy.Field()
    details = scrapy.Field()
    expiration_time = scrapy.Field()
    discount_code = scrapy.Field()
    liked_count = scrapy.Field()
    disliked_count = scrapy.Field()