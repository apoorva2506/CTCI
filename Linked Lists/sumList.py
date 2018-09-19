#SumList 
#reverse the Linked list first

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

	def revList(self):
		curr=self.head
		prev=None
		nextN=None

		while curr is not None:
			nextN=curr.getNextNode()
			curr.setNextNode(prev)	#reverses the link
			prev=curr
			curr= nextN
		self.head=prev
		return self.head

l1 = Linkedlist()

l1.addNode( '6' )
l1.addNode( '1' )
l1.addNode( '7' )

print('added1')

l2 = Linkedlist()

l2.addNode( '2' )
l2.addNode( '9' )
l2.addNode( '5' )

print('added2')

#l.printNode()

revs1 =l1.revList()
reversed_numberList1= []
while revs1 != None:
  reversed_numberList1.append(str(revs1.data))
  revs1=revs1.getNextNode()
reversed_number1=''.join(reversed_numberList1)
print reversed_number1

revs2 =l2.revList()
reversed_numberList2= []
while revs2 != None:
  reversed_numberList2.append(str(revs2.data))
  revs2=revs2.getNextNode()
reversed_number2=''.join(reversed_numberList2)
print type(reversed_number2)

sum_number= int(reversed_number1) + int(reversed_number2)
print type(sum_number)

l3 = Linkedlist()

for i in str(sum_number):
	l3.addNode(i)

l3.printNode()


















