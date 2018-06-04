## CTCI - Arrays and Strings Question 1
## Uses a list as a stack to get a O(n) solution
## Can't do in-place modification on the string since they are immutable in python

def reverse(st):
	st_stack = []
	for ch in st:
		st_stack.append(ch)
	reversed_st = ""
	for ch in st:
		reversed_st = reversed_st+st_stack.pop()
	return reversed_st


print reverse("gozde")
print reverse("")
print reverse()
