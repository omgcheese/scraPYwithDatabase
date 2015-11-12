import scrapy
from scrapy.selector import Selector
from reddit.items import redditItems

class redditSpider(scrapy.Spider):
	name = "reddit"
	allowed_domains = ["reddit.com"]
	start_urls = [
			"https://www.reddit.com/r/gaming/"
			]

	def parse(self, response):
		redditPosts = Selector(response).xpath('//div[@id="siteTable"]')
		items = []
		# count = 0
		for post in redditPosts:
			# count = count + 1
			item = redditItems()
			item['post_title'] = post.xpath('div/div[2]/p[1]/a/text()').extract()
			item['post_link'] = post.xpath('div/div[2]/p[1]/a/@href').extract()
			item['post_rating'] = post.xpath('div/div[1]/div[3]/text()').extract()
			item['post_comment_link'] = post.xpath('div/div[2]//ul/li[1]/a/@href').extract()
			items.append(item)
			print item
			# item['post_sub'] = post.xpath('div[@class="entry"]/p[@class="tagline"]/a/text()').extract()
		
		return items


		
