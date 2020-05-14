"""
Stack Data Structure

"""

class Stack():
	
	def __init__(self):
		self.items = []
	
	def push(self, item):
		self.items.append(item)
		
	def pop(self):
		return self.items.pop()
		
	def isEmpty(self):
		return self.items == []
		
	def peek(self):
		return self.items[-1]
		
	def get_stack(self):
		return self.items
		
s = Stack()
print(s.isEmpty())
s.push("A")
s.push("B")
s.push("C")
print(s.get_stack())
print(s.peek())
s.pop()
print(s.get_stack())