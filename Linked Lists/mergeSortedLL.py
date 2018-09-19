#Merging two sorted Linked Lists 
class Node:
  def __init__(self, data, next):
    self.data = data
    self.next = next   
    
def merge(L1, L2):
  
  # create new linked list pointer
  L3 = Node(None, None)
  prev = L3

  # while both linked lists are not empty
  while L1 != None and L2 != None:
    if L1.data <= L2.data:
      prev.next = L1
      L1 = L1.next
    else:
      prev.next = L2
      L2 = L2.next	
    prev = prev.next

  # once we reach end of a linked list, append the other 
  # list because we know it is already sorted
  if L1 == None:
  	prev.next = L2
  elif L2 == None:
  	prev.next = L1

  return L3.next

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

L3= L1 + L2
while L3 != None:
  print str(L3.data) + ' -> '
  L3 = L3.next


# print the linked list
merged = merge(L1, L2)
# while merged != None:
#   print str(merged.data) + ' -> '
#   merged = merged.next
print 'None'