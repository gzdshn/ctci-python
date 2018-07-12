## CTCI - Chapter 11 - Sorting and Searching Question 5
## Find element in array of strings with empty strings

def search(A,val,start,end):
	if start>end:
		return -1
	
	## Find a midpoint that is not empty
	mid = (start+end)/2
	if A[mid] == "":
		midleft = mid - 1
		midright = mid + 1
		while midleft>=start and midright<=end:
			if A[midright] != "":
				mid = midright
				break
			elif A[midleft] != "":
				mid = midleft
				break
			midright += 1
			midleft -= 1
		if midleft<start and midright>end:
		 	return -1

	## Binary Search with new midpoint
	if A[mid]==val:
		return mid
	elif val<A[mid]:
		return search(A,val,start,mid-1)
	else:
		return search(A,val,mid+1,end)


'''
A = ["at","","","","ball","","","car","","","dad","",""]
print search(A,"ball",0,len(A)-1)
'''