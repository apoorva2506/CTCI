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

	def removeNode(self,value):

	    prev = None
	    curr = self.head  #current node which is to be deleted has head pointed towards it
	    while curr:
	        if curr.getNode() == value:	#checks if the data of current=value
				print(curr.getNode())
				if prev:			#if there is a previous element
					print('prevs')
					prev.setNextNode(curr.getNextNode()) 	#set prev.next=curr.next
				else:
					print('no prevs')
					self.head = curr.getNextNode()		#head=curr.next
				return True
	                
	        prev = curr #set previous one as the current one now
	        curr = curr.getNextNode()
	        
	    return False


l = Linkedlist()

l.addNode( 'a' )
l.addNode( 'b' )
l.addNode( 's' )
l.addNode( 'd' )
l.addNode( 'a' )
l.addNode( 'd' )
#l.printNode()
print('added')

l.removeNode('a')

l.printNode()
