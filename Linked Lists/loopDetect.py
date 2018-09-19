class Node:
	def __init__(self, data, nextNode=None):
		self.data=data
		self.nextNode=nextNode

	def getNode(self):
		return self.data

	def setNode(self,val):
		self.data= val

	def getNextNode(self):
		return self.nextNode

	def setNextNode(self,val):
		self.nextNode = val

class Linkedlist:
	def __init__(self, head=None):
		self.head=head
		self.size=0

	def getSize(self):
	   return self.size

	def addNode(self,data):
	   newNode = Node(data,self.head)
	   self.head = newNode
	   self.size+=1
	   return True
	   
	def printNode(self):
	   curr = self.head
	   while curr:
	       print(curr.data)
	       curr = curr.getNextNode()

	def detectCycle(self):
		slow=self.head
		fast=self.head
		while slow is not None and fast is not None and fast.getNextNode() is not None:
			slow=slow.getNextNode()
			fast=fast.getNextNode().getNextNode()

			if slow.getNode() == fast.getNode():

				print('loop exists')
				return True

	# To find the starting point of the loop, come to a common point,
	# then set one of the pointers to the head and start traversing one by one.
	# where they meet = starting point.

	def findStart(self):
		loopStart=None
		slow=self.head
		fast=self.head
		# print("inside findstart")
		while slow is not None and fast is not None and fast.getNextNode() is not None:
			slow=slow.getNextNode()
			fast=fast.getNextNode().getNextNode()
			if slow.getNode() == fast.getNode():
				#print fast.getNode()
				print("loop")
				break


		slow=self.head
		# print slow.getNode()
		# print fast.getNode()
		while slow != fast:

			slow=slow.getNextNode()
			fast=fast.getNextNode()
			print slow.getNode()
			print fast.getNode()
			loopStart=slow
				
		return loopStart



l1 = Linkedlist()

l1.addNode( '3' )
l1.addNode( '7' )
l1.addNode( '6' )
l1.addNode( '3' )
l1.addNode( '2' )
l1.addNode( '1' )
#l1.printNode()
print('added')
curr=l1.head
curr.getNextNode().getNextNode().getNextNode().getNextNode().getNextNode().setNextNode(curr)
#print curr.getNextNode().getNextNode().getNextNode().getNextNode().getNextNode().getNextNode().getNode()


startpt= l1.findStart()


































