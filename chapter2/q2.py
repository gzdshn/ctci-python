## CTCI - Linked Lists Question 2
## Return kth last element of the list (k=0 returns last element)
## Assumes we know the size of the list
## Assumes we want the value of the element, not the node itself

import sys
sys.path.append('./classes')
from myllist import LinkedList

def returnKthToLast(inlist,k):
	totalSize = inlist.size()
	if totalSize>0:
		stop = totalSize-1-k
		return returnKthToLastHelper(inlist.getHeadNode(),stop,0)
	return None

def returnKthToLastHelper(curr,stop,pos):
	if pos == stop:
		return curr.val
	return returnKthToLastHelper(curr.next,stop,pos+1)


list1 = LinkedList()
for n in [1,2,3,4,5,6]:
	list1.append(n)

for n in [0,1,2,3,4,5]:
	print returnKthToLast(list1,n)

