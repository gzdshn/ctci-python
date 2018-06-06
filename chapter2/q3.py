## CTCI - Linked Lists Question 3
## Delete middle element, given only access to that element

import sys
sys.path.append('./classes')
from myllist import LinkedList

def deleteMiddleElmt(mnode):
	if mnode is None or mnode.next is None:
		return
	curr = mnode
	nextElmt = mnode.next
	while nextElmt.next:
		tmp = curr.next
		curr.val = nextElmt.val
		curr = tmp
		nextElmt = tmp.next
	curr.val = nextElmt.val
	curr.next = None


list1 = LinkedList()
for n in [1,2,3,4,5]:
	list1.append(n)

middleNode = list1.getNode(3)
list1.printList()
deleteMiddleElmt(middleNode)
list1.printList()