P="BATD"
Q="ABACD"


def lcs(x,y):
	if(len(x)==0 or len(y)==0) :
		return (0,"")
	if(x[-1]==y[-1]):
		char = x[-1] 
	
		val,result= lcs(x[:-1],y[:-1])
		
		return (val+1,result+char)
	else:
		t1,result1=lcs(x[:-1],y)
		t2,result2=lcs(x,y[:-1])
		if(t1>t2):
			return (t1,result1)
		else:

			return (t2,result2)

print(lcs(P,Q))
