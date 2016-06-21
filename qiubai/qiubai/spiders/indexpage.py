import scrapy

class QiuBaiSpider(scrapy.Spider):
	name = "qiubai"
	start_urls = [
		"http://www.qiushibaike.com"
	]
	
	def parse(self, response):
		print response.xpath('//div[@class="content"]').extract()
