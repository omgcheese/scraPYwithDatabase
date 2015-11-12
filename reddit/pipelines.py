# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo

class mongodbpipeline(object):

	collection_name = 'REDDIT_POSTS'


	def __init__(self):
		connection = pymongo.MongoClient('mongodb://localhost:27017/')
		db = connection['REDDIT_DATABASE']
		self.collection = db.posts
		print "Pipeline Initiated!"
		# self.collection.insert(
		# 	{
		# 		"test1":	{
		# 		"key1" : "value1",
		# 		"key2" : "value2",
		# 		"key3" : "value3",
		# 		"key4" : "value4",
		# 		"key5" : "value5"
		# 		}
		# 	}
		# 	)
		
		# self.mongo_uri = 'mongodb://localhost:27017/'
		# self.mongo_db = 'REDDIT_DATABASE'

	# def close_spider(self, spider):
	# 	self.connection.close()

	def process_item(self, item, spider):
		print "Processing items....."
		self.collection.insert(dict(item))
		return item
