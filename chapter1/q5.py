## CTCI - Arrays and Strings Question 5
## String Compression
## Assumes lower/upper case letters are different, returns empty string for empty/None input

def compressString(st):
	if st is None or len(st)==0:
		return ""
	
	compressed_st = []
	curr_char = st[0]
	count = 0
	for idx in range(len(st)):
		if st[idx]==curr_char:
			count += 1
		else:
			compressed_st.append(curr_char)
			compressed_st.append(str(count))
			curr_char = st[idx]
			count = 1
	compressed_st.append(curr_char)
	compressed_st.append(str(count))

	compressed_st = "".join(compressed_st)
	if len(compressed_st)>len(st):
		compressed_st = st
	return compressed_st

print compressString("aabbbcdddd")
print compressString("abcd")
print compressString("")
print compressString("AaBBBccPPPPP")
print compressString(None)