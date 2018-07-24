## CTCI - Chapter 4 - Trees and Graphs Question 4
## Given a sorted array create binary tree with least height

class Node():
	def __init__(self,val):
		self.val = val
		self.left = None
		self.right = None

def createDepthLists(Dlists,depth,node):
	if node is None:
		return

	if len(Dlists)>depth:
		Dlists[depth].append(node)
	else:
		Dlists.append([node])

	createDepthLists(Dlists, depth+1, node.left)
	createDepthLists(Dlists, depth+1, node.right)

'''
n1 = Node(5)
n2 = Node(3)
n3 = Node(6)
n4 = Node(1)
n5 = Node(2)
n6 = Node(0)
n7 = Node(4)
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n4.left = n6
n5.right = n7
Dlists = []
createDepthLists(Dlists,0,n1)
for l in Dlists:
	d = []
	for node in l:
		d.append(node.val)
	print d
'''