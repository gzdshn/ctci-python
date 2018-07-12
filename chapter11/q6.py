## CTCI - Chapter 11 - Sorting and Searching Question 6
## Search in a MxN array

def search(A,val):
	currRow = 0
	currCol = len(A[0])-1
	while currRow<len(A) and currCol>=0:
		if A[currRow][currCol] == val:
			return True
		else:
			if A[currRow][currCol]>val:
				currCol -= 1
			else:
				currRow +=1
	return False

'''
A = [[15,20,40,85],[20,35,80,95],[30,55,95,105],[40,80,100,120]]
print search(A,10)
'''