## CTCI - Arrays and Strings Question 3
## Determine whether two strings are a permutation of each other
## Assumes two empty strings are permutations of each other
## Since get/set operations on dicts are on average O(1), runs in O(n) time

def is_permutation(s1,s2):
	if len(s1)!=len(s2):
		return False
	if len(s1)==0:
		return True
	
	charDict1 = {}
	for ch in s1:
		if ch in charDict1:
			charDict1[ch] += 1
		else:
			charDict1[ch] = 0
	charDict2 = {}
	for ch in s2:
		if ch not in charDict1:
			return False
		if ch in charDict2:
			charDict2[ch] += 1
		else:
			charDict2[ch] = 0
	for ch in s2:
		if charDict1[ch] == charDict2[ch]:
			return True
		else:
			return False

print is_permutation("","")
print is_permutation("","a")
print is_permutation("aab","baa")
print is_permutation("gozde","edzog")
print is_permutation("phone","phony")
