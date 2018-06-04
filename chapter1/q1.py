## CTCI - Arrays and Strings Question 1
## Assumes true is returned when a string is empty
## Uses lists, checks whether character already exists - O(n^2) worst case

def uniqueAll(st):
	uniqueList = []
	for character in st:
		found = False
		for elmt in uniqueList:
			if elmt==character:
				found = True
				break
		if not found:
			uniqueList.append(character)

	if len(st)==len(uniqueList):
		return True
	else:
		return False

print uniqueAll("")
print uniqueAll("appalachia")
print uniqueAll("apple")
print uniqueAll("sad")