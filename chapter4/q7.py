## CTCI - Chapter 4 - Trees and Graphs Question 7
## Find common ancestor - Assumed: no parent connection,
## no extra space to hold parent paths, nodes are in the tree

class Node():
	def __init__(self,val):
		self.val = val
		self.left = None
		self.right = None
		self.parent = None


def findCommonAncestor(root,node1,node2):
	if root is None:
		return None

	if root==node1 or root==node2:
		return root

	leftTree = findCommonAncestor(root.left,node1,node2)
	rightTree = findCommonAncestor(root.right,node1,node2)

	if leftTree is not None and rightTree is not None:
		return root
	else:
		return leftTree if leftTree is not None else rightTree

'''
n1 = Node(5)
n2 = Node(3)
n3 = Node(6)
n4 = Node(1)
n5 = Node(4)
n6 = Node(0)
n7 = Node(4.5)
n1.left = n2
n2.parent = n1
n1.right = n3
n3.parent = n1
n2.left = n4
n4.parent = n2
n2.right = n5
n5.parent = n2
n4.left = n6
n6.parent = n4
n5.right = n7
n7.parent = n5
n8 = Node(5.5)
n3.left = n8
n8.parent = n3
print findCommonAncestor(n1,n8,n6).val
'''