## CTCI - Chapter 11 - Sorting and Searching Question 3
## Find element in rotated array

def searchRotated(A,val,start,end):
	mid = (start+end)/2
	if A[mid]==val:
		return mid
	if start>end:
		return -1

	if A[start]<A[mid]:
		if val>=A[start] and val<=A[mid]:
			return searchRotated(A,val,start,mid-1)
		else:
			return searchRotated(A,val,mid+1,end)
	elif A[mid]<A[start]:
		if val>=A[mid] and val<=A[end]:
			return searchRotated(A,val,mid+1,end)
		else:
			return searchRotated(A,val,start,mid-1)
	elif A[mid]==A[start]:
		if A[mid]!=A[end]:
			return searchRotated(A,val,mid+1,end)
		else:
			idx = searchRotated(A,val,mid+1,end)
			if idx == -1:
				return searchRotated(A,val,start,mid-1)
			else:
				return idx

'''
A = [15,16,19,20,25,1,3,4,5,7,10,14]
#A = [2,2,2,3,4,2]
print searchRotated(A,5,0,len(A)-1)
'''