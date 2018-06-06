## CTCI - Arrays and Strings Question 7
## If an element of an MxN matrix is zero, set row and column to zero

from sets import Set

def setZero(M):
	toSetRow = Set()
	toSetCol = Set()
	for idx in range(len(M)):
		for idy in range(len(M[0])):
			if M[idx][idy] == 0:
				toSetRow.add(idx)
				toSetCol.add(idy)

	for idx in range(len(M)):
		for idy in range(len(M[0])):
			if idx in toSetRow or idy in toSetCol:
				M[idx][idy] = 0

M1 = [[1,2,3],[4,0,6],[7,8,9]]
setZero(M1)
print M1
M2 = [[1,0,3,4],[5,6,7,8],[9,10,11,12]]
setZero(M2)
print M2