## CTCI - Chapter 11 - Sorting and Searching Question 1
## Merge Two Sorted Arrays in Place

def mergeSortedArrays(A,B): ## O(N^2) solution
	for idx in range(len(B)):
		idy = 0
		while A[idy]<B[idx]:
			idy += 1
		for idz in range(len(B)+idx,idy-1,-1):
			if idz+1 < len(A):
				A[idz+1] = A[idz]
		A[idy] = B[idx]
		print A

def mergeSortedArraysBetter(A,B): ## O(N) solution
	idx = len(B)-1
	idy = len(B)-1
	idz = len(A)-1
	while idz>=0:
		if idx>=0 and idy>=0:
			if A[idx]>=B[idy]:
				A[idz] = A[idx]
				idx -= 1
			else:
				A[idz] = B[idy]
				idy -= 1
		elif idx<0 and idy>=0:
			A[idz] = B[idy]
			idy -= 1
		idz -= 1
'''
B = [1,4,5,6,9,13,14]
A = [2,3,7,8,10,11,12] + [None]*len(B) 
mergeSortedArraysBetter(A,B)
print A
'''
