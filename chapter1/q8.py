## CTCI - Arrays and Strings Question 8
## Check if one string is the rotation of the other considerin you have a isSubstring() method

def isRotationBrute(s1,s2):
	if s1 is None or s2 is None:
		return False
	if len(s1) != len(s2):
		return False

	for idx in range(len(s1)):
		new_st = s1[idx:] + s1[:idx] # bad because this is essentially O(n)
		if new_st in s2:
			return True
	return False

def isRotationBetter(s1,s2):
	if s1 is None or s2 is None:
		return False
	if len(s1) != len(s2):
		return False

	if s2 in s1+s1:
		return True
	else:
		return False


print isRotationBetter("hello","elloh")
print isRotationBetter("ih","hi")
print isRotationBetter("gozde","degoz")
print isRotationBetter("w","k")

