class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
	

class LinkedList:
	def __init__(self):
		self.head = None
		
	def addNode(self, data):
		newNode = Node(data)
		if self.head == None:
			self.head = newNode
		else:
			temp = self.head
			while temp.next != None:
				temp = temp.next
			temp.next = newNode
	
	def getList(self):
		temp = self.head
		while temp != None:
			print(temp.data, end=" ")
			temp = temp.next
		print("\n")
			
	def deleteNode(self,value):
		
		if self.head.data == value:
			self.head = self.head.next
		else:
			temp = self.head
			while temp.next != None:
				if temp.next.data == value:
					temp.next = temp.next.next
				temp = temp.next

#l = LinkedList()
#l.addNode(5)
#l.addNode(3)
#l.addNode(2)
#l.getList()
#print("\n")
#l.deleteNode(3)
#l.getList()
#print("\n")
#l.addNode(1)
#l.addNode(4)
#l.getList()
#print("\n")
#l.deleteNode(5)
#l.getList()