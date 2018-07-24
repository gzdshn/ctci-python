## CTCI - Chapter 4 - Trees and Graphs Question 1
## Function to balance a Tree (assumes a tree was given)

def getHeight(node):
	if node==None:
		return 0

	leftH = getHeight(node.left)
	righH = getHeight(node.right)
	if getHeight(node.left) == -1:
		return -1
	if getHeight(node.right) == -1:
		return -1

	heightDiff = abs(leftH - righH)

	if heightDiff<=1:
		return max(leftH,rightH) + 1
	else:
		return -1

def isBalanced(node):

	if getHeight(node) == -1:
		return False
	else:
		return True

