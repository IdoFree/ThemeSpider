from themespider.http.request import request
from themespider.core import dispatcher
import queue 
class Spider:
	def __init__(self,name,seed_list = None):
		if seed_list not None:
			self.seed_list = seed_list
		else:
			self.seed_list = queue.Queue()
		self.name = name
		pass
		
	def start():
		while True:
			if len(seed_list) == 0 :
				seed_list.extend(dispatcher.seedDispatcher.getNextUrls(10))
			else:				
				response = request.get(seed_list.get())
				links = response.get_all_links()
				
				for link in links:
					seedQueue.put(link)						
				#TODO persist the response data  
				content = response.content
		
		
		
	