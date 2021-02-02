import scrapy
from scrapy.spiders import CrawlSpider, Rule, Request
from scrapy.linkextractors import LinkExtractor ##配合Rule进行URL规则匹配
# 引入自定义的items
from MySpider.items import MyspiderItem

# # 继承scrapy.Spider
class NovelSpider(scrapy.Spider):
    # 爬虫名
    name = 'MySpider'
    # 允许的域名
    allowed_domains = ['jmvbt.com/',"google.com/","baidu.com/"]
    # 入口url 扔到调度器里面去
    # start_urls = ['https://jmvbt.com/']
    start_urls = ["https://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=trump"]

    rules = (
        Rule(LinkExtractor(allow=('\.html',)), callback='parse_item', follow=True),
    )

    def parse(self, response):
        # for sel in response.xpath('//ul/li'):
        #     item = MyspiderItem()
        #     item['title'] = sel.xpath('a/text()').extract()
        #     item['link'] = sel.xpath('a/@href').extract()
        #     item['desc'] = sel.xpath('text()').extract()
        #     yield item
        # item = MyspiderItem()
        # item['url'] = response.url
        # item['category'] = response.xpath('//*[@id="content"]/div[1]/div[1]/span[2]/a/text()').extract()[0]
        # item['title'] = response.xpath('//*[@id="content"]/div[1]/h1/text()').extract()[0]
        # item['imgurl'] = response.xpath('//*[@id="post_content"]/p/img/@src').extract()
        # print(item)
        print("=========url=======")
        print("img:"+response.url)
        for sel in response.xpath('//img/@src'):
            # item = MyspiderItem()
            # item["imgurl"] = 
            print("=======sel=======")
            print(sel.extract())
            # yield item