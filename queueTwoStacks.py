"""
Implementing a Queue using Two Stacks

"""

from stack import Stack

class MyQueue:
	def __init__(self):
		self.newestDataOnTop = Stack()
		self.oldestDataOnTop = Stack()
		self.popCount = 0 #keeps track of when newestData gets popped
		self.pushCount = 0

	def enqueue(self, data):
		self.newestDataOnTop.push(data)
	
	def dequeue(self):
		temp = Stack()
		if self.newestDataOnTop.isEmpty():
			return self.oldestDataOnTop.pop()
		else:
			while not self.oldestDataOnTop.isEmpty():
				temp.push(self.oldestDataOnTop.pop())

			while not self.newestDataOnTop.isEmpty():
				self.oldestDataOnTop.push(self.newestDataOnTop.pop())

			while not temp.isEmpty():
				self.oldestDataOnTop.push(temp.pop())
			return self.oldestDataOnTop.pop()


	def get_queue(self):
		temp = Stack()
		if self.newestDataOnTop.isEmpty():
			return self.oldestDataOnTop.get_stack()
		else:
			while not self.oldestDataOnTop.isEmpty():
				temp.push(self.oldestDataOnTop.pop())

			while not self.newestDataOnTop.isEmpty():
				self.oldestDataOnTop.push(self.newestDataOnTop.pop())

			while not temp.isEmpty():
				self.oldestDataOnTop.push(temp.pop())
			return self.oldestDataOnTop.get_stack()



	def peek(self):

		if self.oldestDataOnTop.isEmpty():
			while not self.newestDataOnTop.isEmpty():
				self.oldestDataOnTop.push(self.newestDataOnTop.pop())
				self.popCount+=1
			return self.oldestDataOnTop.peek()
		else:
			return self.oldestDataOnTop.peek()



# m = MyQueue()

# m.enqueue("Song 1")
# m.enqueue("Song 2")
# m.enqueue("Song 3")
# print(m.get_queue())
# m.dequeue()
# print(m.get_queue())
# m.enqueue("Song 4")
# m.enqueue("Song 5")
# print(m.get_queue())
# m.dequeue()
# print(m.get_queue())
