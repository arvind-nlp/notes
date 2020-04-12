def perm(s, acc):

	if(len(s)==0):
		print(acc)
	for i in range(len(s)):
		current = s[i]
		remaining = s[0:i] + s[i+1:]
		perm(remaining, acc+current)


perm("abc","")
