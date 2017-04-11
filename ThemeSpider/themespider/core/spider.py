from themespider.http.request import request
class Spider:
	def __init__(self,name,seed_list = None):
		if seed_list not None:
			self.seed_list = seed_list
		else:
			self.seed_list = []
		self.name = name
		pass
		
	def start():
		response = request.get(url)
		response.get_all_links()
		
	