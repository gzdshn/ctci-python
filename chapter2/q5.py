## CTCI - Linked Lists Question 5
## Sum numbers that occur in a list in reverse/forward order
## Recursive solution, runs in O(n+m)

import sys
sys.path.append('./classes')
from myllist import LinkedList

def sumReverse(head1,head2):
	return sumReverseHelper(head1,head2,1)

def sumReverseHelper(head1,head2,multiplier):
	if head1 is None and head2 is None:
		return 0
	if head1 is not None and head2 is None:
		return head1.val*multiplier + sumReverseHelper(head1.next,None,multiplier*10)
	elif head1 is None and head2 is not None:
		return head2.val*multiplier + sumReverseHelper(None,head2.next,multiplier*10)
	else:
		return head1.val*multiplier + head2.val*multiplier + sumReverseHelper(head1.next,head2.next,multiplier*10)

def sumForward(head1,head2):
	max_multiplier = findMaxMultiplier(head1,head2)
	return sumForwardHelper(head1,head2,max_multiplier)

def sumForwardHelper(head1,head2,multiplier):
	if head1 is None and head2 is None:
		return 0
	if head1 is not None and head2 is None:
		return head1.val*multiplier + sumForwardHelper(head1.next,None,multiplier/10)
	elif head1 is None and head2 is not None:
		return head2.val*multiplier + sumForwardHelper(None,head2.next,multiplier/10)
	else:
		return head1.val*multiplier + head2.val*multiplier + sumForwardHelper(head1.next,head2.next,multiplier/10)

def findMaxMultiplier(head1,head2):
	length1 = 0
	curr = head1
	while curr:
		length1 +=1
		curr = curr.next
	length2 = 0
	curr = head2
	while curr:
		length2 +=1
		curr = curr.next	
	return pow(10,max(length1,length2)-1)


list1 = LinkedList()
for n in [7,1,6]:
	list1.append(n)

list2 = LinkedList()
for n in [5,9,2]:
	list2.append(n)

headNode1 = list1.getHeadNode()
headNode2 = list2.getHeadNode()
print sumReverse(headNode1,headNode2)
print sumForward(headNode1,headNode2)
