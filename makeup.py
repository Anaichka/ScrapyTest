import scrapy
from model import CosmeticItem

class MakeupSpide(scrapy.Spider):

    name = "make_up"
    start_urls = ['https://makeup.com.ua/categorys/195413/']

    custom_settings = {
        'FEED_EXPORT_ENCODING': 'utf-8'
    }

    def parse(self, response, **kwargs):
        products = response.xpath('//div[@class="simple-slider-list__link"]/a/@href').extract()
        for product in products:
            yield scrapy.Request(response.urljoin(product), self.parse_product)

    def parse_product(self, response):
        item = CosmeticItem()
        item['url'] = response.url
        item['name'] = response.xpath('//div[@itemprop="name"]/text()').extract_first()
        item['price'] = response.xpath('//span[@itemprop="price"]/text()').extract_first()
        item['category'] = response.xpath('//div[@class="product-item__category"]/text()').extract_first()
        yield item

