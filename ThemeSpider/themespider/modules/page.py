import datetime
class Page:
	DEFAULT_CHARSET = 'uft-8'
	def __init__(self,title=None,content=None):
		self.charset = DEFAULT_CHARSET
		self.title = title
		self.content = content
		self.create_time = datetime.now()