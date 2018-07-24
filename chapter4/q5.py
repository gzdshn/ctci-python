## CTCI - Chapter 4 - Trees and Graphs Question 5
## Check if a given binary tree is a binary search tree

class Node():
	def __init__(self,val):
		self.val = val
		self.left = None
		self.right = None

def isBinarySearch(node,minLimit,maxLimit):
	if node is None:
		return True

	leftTree = True 
	if node.left is not None:
		leftTree = isBinarySearch(node.left,minLimit,node.val)
	rightTree = True
	if node.right is not None:
		rightTree = isBinarySearch(node.right,node.val,maxLimit)

	if leftTree and rightTree and node.val<maxLimit and node.val>=minLimit:
		return True
	else:
		return False

'''
n1 = Node(5)
n2 = Node(3)
n3 = Node(6)
n4 = Node(1)
n5 = Node(4)
n6 = Node(0)
n7 = Node(8)
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n4.left = n6
n5.right = n7
n3.left = Node(1)
print isBinarySearch(n1,-float('inf'),float('inf'))
'''