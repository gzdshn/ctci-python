## CTCI - Chapter 11 - Sorting and Searching Question 2
## Sort array of strings so that anagrams are next to each other

def sortByAnagram(A):
	sortedList = []
	anagramMap = dict()
	for st in A:
		stkey = "".join(sorted(st))
		if stkey in anagramMap:
			anagramMap[stkey].append(st)
		else:
			anagramMap[stkey] = [st]
	for key in anagramMap.keys():
		sortedList.extend(anagramMap[key])
	return sortedList
