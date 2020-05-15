"""
Queue Data Structure, using list

"""

class Queue:
	
	def __init__(self):
		self.items = []
	
	def peek(self):
		return self.items[0]
	
	def enqueue(self, data):
		self.items.append(data)
	
	def dequeue(self):
		self.items.pop(0)
		
	def isEmpty(self):
		return self.items == []
	
	def get_queue(self):
		return self.items
		
q = Queue()
print(q.isEmpty())
q.enqueue("Song 1")
q.enqueue("Song 2")
q.enqueue("Song 3")
print(q.get_queue())
q.dequeue()
print(q.get_queue())