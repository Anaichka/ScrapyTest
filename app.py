from scrapy.crawler import CrawlerProcess
from makeup import MakeupSpide
from parfums import ParfumsSpide

process = CrawlerProcess(settings={
    "FEEDS": {
        "items.json": {"format": "json"},
    },
})

process.crawl(ParfumsSpide)
process.crawl(MakeupSpide)
process.start()