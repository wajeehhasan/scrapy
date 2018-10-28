import scrapy
import re
class BookSpider(scrapy.Spider):
	name='bookspider'
	start_urls=["http://books.toscrape.com/"]
	def parse(self, response):
		tit=[]
		tit_s=''
		pri=[]
		pri_s=""
		for titles in response.css("article[class='product_pod']"):
			yield{
				'title':titles.css("h3>a::attr(title)").extract(),
				'price':titles.css("div[class='product_price']>p[class='price_color']::text").extract_first()
			}