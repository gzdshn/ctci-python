## CTCI - Linked Lists Question 7
## Check if a linked list is a palindrome
## Basically runs in O(2n)~O(n) time, O(n) space
## If we had a doubly linked list (with a tail pointer), we could have done this in O(n/2)

import sys
sys.path.append('./classes')
from myllist import LinkedList

def getReversedList(head_in):
	list_new = LinkedList()
	curr = head_in
	while curr:
		list_new.insert(curr.val,0)
		curr = curr.next
	return list_new.getHeadNode()

def isPalindrome(head1):
	head2 = getReversedList(head1)
	while head1:
		if head1.val != head2.val:
			return False
		head1 = head1.next
		head2 = head2.next
	return True

list1 = LinkedList()
for n in "":
	list1.append(n)

print isPalindrome(list1.getHeadNode())