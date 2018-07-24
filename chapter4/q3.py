## CTCI - Chapter 4 - Trees and Graphs Question 3
## Given a sorted array create binary tree with least height

class Node():
	def __init__(self,val):
		self.val = val
		self.left = None
		self.right = None

def createBST(A,start,end):
	if start>end:
		return None

	mid = (start+end)/2
	newNode = Node(A[mid])
	newNode.left = createBST(A,start,mid-1)
	newNode.right = createBST(A,mid+1,end)

	return newNode


A = [1,2,3,4,5,6,7,8,9,10]
treeRoot = createBST(A,0,len(A)-1)