## CTCI - Chapter 4 - Trees and Graphs Question 6
## Find successor

class Node():
	def __init__(self,val):
		self.val = val
		self.left = None
		self.right = None
		self.parent = None

def findSuccessor(node):
	if node is None:
		return None

	if node.right is not None:
		rightNode = node.right
		while rightNode.left is not None:
			rightNode = rightNode.left
		return rightNode
	else:
		parentNode = node.parent
		curr = node
		while parentNode is not None and parentNode.right == curr:
			curr = parentNode
			parentNode = parentNode.parent
		return parentNode

	return None

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
print findSuccessor(n6).val
'''