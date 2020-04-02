#knapsack
#https://www.youtube.com/watch?v=ipRGyCcbrGs

w = [2,2,4,5]
v = [3,7,2,9]
N = 4
CAP = 10

# maximum value got by including i..N
def f(i,capacity):
	if(i==N-1):
		if(w[i]<capacity): return v[i]
		else: return 0 
	include =  v[i] + f(i+1, capacity-w[i])
	exclude = f(i+1, capacity)
	return max(include,exclude)

print(f(0,CAP))
