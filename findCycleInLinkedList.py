from singlyLinkedList import LinkedList as linked
"""
Original Solution



def findCycleInLinkedList(linkedlist):
	if(linkedlist.head == None):
		print("Empty")
	else:
		visited= []
		temp = linkedlist.head
		while temp != None:
			if temp.data in visited:
				print("There is a cycle")
				return 
			else:
				visited.append(temp.data)
				temp = temp.next
		print("There is not a cycle")
"""

def findCycleInLinkedList(linkedlist):
	
	if linkedlist.head == None:
		print("Empty")
		return
	
	if linkedlist.head.next is None or linkedlist.head.next.next is None:
		print("No Cycle")
		return
	
	tracker1 = linkedlist.head
	tracker2 = linkedlist.head.next.next
	
	while tracker1 != None:
		print("Tracker 1:", tracker1.data, "Tracker 2:", tracker2.data)
		if tracker1.data == tracker2.data:
			print("There is a cycle")
			return
		tracker1 = tracker1.next
		
		if tracker2.next == None:
			if tracker2.data == linkedlist.head.data:
				print("There is a cycle")
				return
			else:
				tracker2 = linkedlist.head.next
		elif tracker2.next.next == None:
			if tracker2.next.data == linkedlist.head.data:
				print("There is a cycle")
				return
			else:
				tracker2 = linkedlist.head
		else:
			if tracker2.next == None:
				tracker2 = linkedlist.head.next
			else:
				tracker2 = tracker2.next.next
				
	print("No Cycle")							
																
f = linked()
f.addNode(5)
f.addNode(6)
f.addNode(7)
#f.getList()
#findCycleInLinkedList(f)
f.addNode(8)
f.addNode(6)
f.getList()
findCycleInLinkedList(f)