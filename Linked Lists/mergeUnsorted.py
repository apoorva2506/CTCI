#Merging two Unsorted Linked Lists 
class Node:
	def __init__(self, data, next):
		self.data = data
		self.next = next   

def merge(L1, L2):
	while L1 is not None:
		# print('inside l1')
		a= L1
		if L1.next is None:
			# print("inside last")
			last=a
			# return last
		L1=L1.next
	last.next = L2

# create first linked list: 1 -> 3 -> 10
n3 = Node(10, None)
n2 = Node(3, n3)
n1 = Node(1, n2)
L1 = n1

# while L1 != None:
#   print str(L1.data) + ' -> '
#   L1 = L1.next

# create second linked list: 5 -> 8 -> 9
n6 = Node(9, None)
n5 = Node(6, n6)
n4 = Node(5, n5)
L2 = n4

merged = merge(L1, L2)

while L1 is not None:
	print L1.data
	L1= L1.next

