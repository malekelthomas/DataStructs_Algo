class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None
	

class DoublyLinkedList:
	def __init__(self):
		self.head = None
		self.tail = None
		
	def addNode(self, data):
		newNode = Node(data)
		if self.head == None:
			self.head = newNode
			self.head.prev = None
			self.tail = newNode
			self.tail.next = None
		else:
			temp = self.tail
			temp.next = newNode
			self.tail = temp.next
			self.tail.prev = temp
	def getList(self):
		temp = self.head
		while temp != None:
			print(temp.data, end=" ")
			temp = temp.next
			
	def getListReverse(self):
		temp = self.tail
		while temp != None:
			print(temp.data, end=" ")
			temp = temp.prev
			
	def deleteFromFront(self):
		if self.head == None:
			return 
		else:
			self.head = self.head.next
			self.head.prev = None
			
		
	def deleteNode(self,value):
		
		if self.head.data == value:
			self.head = self.head.next
			self.head.prev = None
		elif self.tail.data == value:
			self.tail = self.tail.prev
			self.tail.next = None
		else:
			temp = self.head
			while temp.next != None:
				if temp.next.data == value:
					temp.next.next.prev = temp.next.prev
					temp.next = temp.next.next
				temp = temp.next
				
d = DoublyLinkedList()
d.addNode(5)
d.addNode(6)
d.addNode(7)
d.addNode(8)
d.getList()
print("\n")
d.getListReverse()
print("\n")
d.deleteNode(6)
d.getList()
print("\n")
d.deleteNode(5)
d.getList()
print("\n")
d.deleteNode(8)
d.getList()