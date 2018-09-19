#Check if Linked List is Palindrome
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
	   # while curr:
	   #     print(curr.data)
	   #     curr = curr.getNextNode()
	   return curr

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

	def isEqualOrNot(self,ll1,ll2):
		while ll1 is not None and ll2 is not None:
			print('dnn')
			if ll1.getNode() == ll2.getNode():
				# print("Palindrome")
				return True
			else:
				# print("Not Plaindrome")
				return False

l1 = Linkedlist()

l1.addNode( '1' )
l1.addNode( '2' )
l1.addNode( '1' )

print('added1')
linklis1= l1.printNode()

while linklis1 is not None:
	print linklis1.getNode()
	linklis1=linklis1.getNextNode()

reversed_list=l1.revList()

while reversed_list is not None:
	print reversed_list.getNode()
	reversed_list=reversed_list.getNextNode()

def isEqualOrNot(linklis1,reversed_list):
		while linklis1 is not None and reversed_list is not None:
			print('dnn')
			if linklis1.getNode() == reversed_list.getNode(): #not working yet
				print("Palindrome")
				return True
			else:
				print("Not Plaindrome")
				return False

res = isEqualOrNot(linklis1,reversed_list)
print(res)




















