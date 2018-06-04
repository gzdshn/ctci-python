## CTCI - Arrays and Strings Question 1
## Assumes true is returned when a string is empty
## Uses sets, set look-up time O(1) in average case in python
## Addition for max number of characters check
from sets import Set

MaxNumChar = 128
def uniqueAll(st):
	if len(st)>MaxNumChar:
		return False
	uniqueSet = Set()
	for character in st:
		if character in uniqueSet:
			return False
		else:
			uniqueSet.add(character)

	return True

print uniqueAll("")
print uniqueAll("appalachia")
print uniqueAll("apple")
print uniqueAll("sad")