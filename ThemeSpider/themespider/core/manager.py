import queue

class SeedManager:
	__q = queue.Queue(1000)
	
	def getNextSeed(self):
		if(!__q.empty()):
			return __q.get()#set true to block if the the queue is empty
		else:
			print "the seed queue is empty"
			
	def putSeed(self,url):
		if(!__q.full()):
			__q.put(url)
		else:
			print "the seed queue is full"

seedManager = seedManager()