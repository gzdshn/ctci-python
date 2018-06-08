## CTCI - Linked Lists Question 6
## Return node at the beginning of loop

import sys
sys.path.append('./classes')
from myllist import LinkedList
from sets import Set

def returnLoopNode(head):
	if head is None:
		return None
	itemSet = Set()
	runner = head
	itemSet.add(head)
	while runner.next:
		if runner.next in itemSet:
			return runner.next
		itemSet.add(runner.next)
		runner = runner.next
	return None


list1 = LinkedList()
for n in [1,2,3,4,5,6]:
	list1.append(n)

endNode = list1.getNode(5)
loopNode = list1.getNode(2)
endNode.next = loopNode

headNode = list1.getHeadNode()
result = returnLoopNode(headNode)
if result:	
	print result.val
else:
	print result



