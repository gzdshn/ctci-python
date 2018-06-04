## CTCI - Arrays and Strings Question 2
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

def reverseBetter(st):
	if len(st)>0:
		return st[::-1]
	return ""

print reverseBetter("gozde")
print reverseBetter("")
print reverseBetter("a")
