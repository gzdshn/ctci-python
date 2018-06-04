## CTCI - Arrays and Strings Question 4
## Replaces all empty space with the string "%20"
## Assumes given string will not be None, returns empty string for empty string input

def replaceSpace(st):
	if len(st)==0:
		return ""
	if st.isspace():
		return "%20"
	leading = True if st[0].isspace() is True else False
	trailing = True if st[-1].isspace() is True else False
	st.rstrip()
	st.lstrip()
	st_parts = st.split()
	new_st = ""
	if leading:
		new_st += "%20"
	new_st += "%20".join(st_parts)
	if trailing:
		new_st += "%20"
	return new_st

print replaceSpace("	Mr  John \nSmith	")
print replaceSpace("		")