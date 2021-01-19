import scrapy


class CosmeticItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    category = scrapy.Field()
    url = scrapy.Field()
