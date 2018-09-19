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

	def removeDups(self):
		curr = self.head
		prev=None
		newList=[]
		while curr is not None:
			#print(curr.getNode())
			if curr.getNode() in newList:
				prev.setNextNode(curr.getNextNode()) 	#set prev.next=curr.next
				curr = curr.getNextNode()
				# if prev:			#if there is a previous element
				# 	print('prevs')
				# else:
				# 	print('no prevs')
				# 	self.head = curr.getNextNode()		#head=curr.next
				# 	prev = curr #set previous one as the current one now
				# 	curr = curr.getNextNode()
				# return True

			else:
				newList.append(curr.data)
				prev = curr #set previous one as the current one now
				curr = curr.getNextNode()


l = Linkedlist()

l.addNode( 'a' )
l.addNode( 'b' )
l.addNode( 'a' )
l.addNode( 'd' )
l.addNode( 'a' )
l.addNode( 'c' )
l.printNode()
print('added')

l.removeDups()

l.printNode()