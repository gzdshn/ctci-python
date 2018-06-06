## CTCI - Linked Lists Question 4
## Partition Linked List around a value x

import sys
sys.path.append('./classes')
from myllist import LinkedList

def partition(head,x):
	if head is None:
		return
	
	searcher = head
	partitioner = head
	while partitioner and partitioner.val <= x:
		partitioner = partitioner.next
		searcher = searcher.next

	while searcher:
		if searcher.val > x:
			searcher = searcher.next
		else:
			smallVal = searcher.val
			searcher.val = partitioner.val
			partitioner.val = smallVal
			partitioner = partitioner.next
			searcher = searcher.next


list1 = LinkedList()
for n in [6,2,3,4,5,7]:
	list1.append(n)

headNode = list1.getHeadNode()
list1.printList()
partition(headNode,3)
list1.printList()

