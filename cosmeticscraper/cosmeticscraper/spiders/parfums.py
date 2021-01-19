import scrapy
from ..items import CosmeticItem


class ParfumsSpide(scrapy.Spider):

    name = "parfums"
    start_urls = ['https://parfums.ua/category/salonnaya-kosmetika/brand=klapp']

    custom_settings = {
        'FEED_EXPORT_ENCODING': 'utf-8'
    }

    def parse(self, response, **kwargs):
        products = response.xpath('//div[@class="product_info"]/a/@href').extract()
        for product in products:
            yield scrapy.Request(response.urljoin(product), self.parse_product)

    def parse_product(self, response):
        item = CosmeticItem()
        item['url'] = response.url
        item['name'] = response.xpath('//h1[contains(@class,"product_name")]/text()').extract_first()
        item['price'] = response.xpath('//span[@class="price_num"]/text()').extract_first()
        item['category'] = response.xpath('//div[contains(text(), "Категория:")]/following-sibling::div/a/span/text()').extract_first()
        yield item
