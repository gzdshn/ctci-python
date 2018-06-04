## CTCI - Arrays and Strings Question 6
## Rotate Image 90 degrees
import numpy as np

def rotateMatrix(M,start,end):
	if start > end or start == end:
		return
	rotateMatrix(M,start+1,end-1)
	top = M[start,start:end+1].copy()
	M[start,start:end+1] = (M[start:end+1,start])[::-1]
	M[start:end+1,start] = M[end,start:end+1]
	M[end,start:end+1] = M[start:end+1,end][::-1]
	M[start:end+1,end] = top
	
def rotate(M):
	rotateMatrix(M,0,len(M)-1)

M1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
rotate(M1)
print M1
M2 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
rotate(M2)
print M2

## Alternative trick with zip
M3 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print zip(*M3[::-1])