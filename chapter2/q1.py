## CTCI - Linked Lists Question 1
## Remove duplicates from an unsorted linked list

import sys
sys.path.append('./classes')
from myllist import LinkedList
from sets import Set

def removeDuplicates(inlist):
	if inlist.size()>1:
		valSet = Set()
		prev = inlist.getHeadNode()
		valSet.add(prev.val)
		curr = prev.next
		while curr:
			if curr.val in valSet:
				prev.next = curr.next
				curr = prev.next
			else:
				valSet.add(curr.val)
				prev = curr
				curr = curr.next
				


list1 = LinkedList()
for n in [1,2,2,3,4,4,4,5]:
	list1.append(n)
list1.printList()

removeDuplicates(list1)
list1.printList()

list2 = LinkedList()
for n in [2,1,3,2,4,5,4,6,5,5]:
	list2.append(n)
list2.printList()

removeDuplicates(list2)
list2.printList()	

list3 = LinkedList()
list3.printList()

removeDuplicates(list3)
list3.printList()
