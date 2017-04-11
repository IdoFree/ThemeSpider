import PriorityQueue from queue

class SeedQueue:
	queue = None
	def __init__(self,size=1000):
		queue = PriorityQueue(size)
		
	def get():
		return queue.get()
		
	def put(ob):
		queue.put(ob)
		
seedQueue = SeedQueue()