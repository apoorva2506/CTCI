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

	def remDups_withoutbuffer(self):
		curr = self.head
		
		while curr is not None:
			# print(curr.getNextNode().getNode())
			runner = curr
			while runner.getNextNode() is not None:
				
				if runner.getNextNode().getNode() == curr.getNode():
					#print('inside equal')
					# print(runner.getNextNode().getNode())
					# print(curr.getNode())
					runner.setNextNode(runner.getNextNode().getNextNode())
				else:
					#print('inside nt equal')
					runner=runner.getNextNode()
			curr=curr.getNextNode()


l = Linkedlist()

l.addNode( 'a' )
l.addNode( 'b' )
l.addNode( 'a' )
l.addNode( 'd' )
l.addNode( 'a' )
l.addNode( 'c' )
#l.printNode()
print('added')

l.remDups_withoutbuffer()

l.printNode()