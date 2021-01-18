from scrapy.item import Item, Field

class CosmeticItem(Item):
    name = Field()
    price = Field()
    category = Field()
    url = Field()
