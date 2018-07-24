## CTCI - Chapter 4 - Trees and Graphs Question 9
## Print all paths that sum to given value

class Node():
	def __init__(self,val):
		self.val = val
		self.left = None
		self.right = None


def getSumPaths(node,sumVal,pathList):
	if node is None:
		return

	pathList.append(node)

	sumPath = 0
	printPath = []
	for idx in range(len(pathList)-1,-1,-1):
		sumPath += node.val
		printPath.append(pathList[idx].val)
		if sumPath == sumVal:
			print printPath[::-1]

	getSumPaths(node.left,sumVal,pathList)
	getSumPaths(node.right,sumVal,pathList)

	pathList.pop()


