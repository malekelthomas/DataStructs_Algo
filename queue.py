"""
Queue Data Structure, using list

"""

class Queue:
	
	def __init__(self):
		self.items = []
	
	def peek(self):
		return self.items[0]
	
	def add(self, data):
		self.items.append(data)
	
	def remove(self):
		self.items.pop(0)
		
	def isEmpty(self):
		return self.items == []
	
	def get_queue(self):
		return self.items
		
q = Queue()
print(q.isEmpty())
q.add("Song 1")
q.add("Song 2")
q.add("Song 3")
print(q.get_queue())
q.remove()
print(q.get_queue())