from themespider.http.request import request
from themespider.core import dispatcher

from . import SeedManager

import queue 
class Spider:
	def __init__(self,name):	
		self.name = name
		pass
		
	def start():
		while True:
			''' when start crawling , the spider will get the initialized url from seedDispatcher
				then parsing the response , and will put the url in the response body to the seedDispatcher 
			'''
			seed_list = dispatcher.seedDispatcher.getNextUrls(10)
			for seed : range(seed_list):
				response = request.get(seed)
				links = response.get_all_links()
				for link in links:
					seedManager.put(link)			
				content = response.content
				self.parse(content)
				print content
		
		
	
	
	def parse(self,content):
		print "default parse behaviour"
		pass
		
	