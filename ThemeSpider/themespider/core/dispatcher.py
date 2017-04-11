from threading import Thread
class SeedDispatcher:
	"""
	this class is for monitoring the crawling seed , and dispatcher 
	the target seed from SeedQueue into the next spider
	"""
	#thread1 = Thread(target = function01, args = (10,'thread1', ))
    #thread1.start()
	
	
	
	def getNextUrls(count=10):
		resultUrls = []
		for i in range(10):
			resultUrls[i] =  seedQueue.get()
		return resultUrls
	
	
	

seedDispatcher = SeedDispatcher()
	