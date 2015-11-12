import scrapy
from scrapy.selector import Selector
from reddit.items import redditItems

class redditSpider(scrapy.Spider):
	#reddit crawler attributes

	name = "reddit"
	allowed_domains = ["reddit.com"]
	start_urls = [
			"https://www.reddit.com/r/gaming/"
			]
	print "Crawling..." + name;

	def parse(self, response):
		print "Extraction and Parsing Initiated!"
		redditPosts = Selector(response).xpath('//div[@id="siteTable"]')
		items = []
		
		for post in redditPosts:
			# extracting post titles, links, ratings
			item = redditItems()
			item['post_title'] = post.xpath('div/div[2]/p[1]/a/text()').extract()
			item['post_link'] = post.xpath('div/div[2]/p[1]/a/@href').extract()
			item['post_rating'] = post.xpath('div/div[1]/div[3]/text()').extract()
			item['post_comment_link'] = post.xpath('div/div[2]//ul/li[1]/a/@href').extract()
			items.append(item)
			# item['post_sub'] = post.xpath('div[@class="entry"]/p[@class="tagline"]/a/text()').extract()
		
		return items


		
