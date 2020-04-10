arr=[-2,1,-3,4,-1,2,1,-5,4]


local_max = 0
global_max= 0

print(arr)
for item in arr:

	local_max = max(0,local_max+item)
	print(local_max)
	if(local_max>global_max):
		global_max=local_max

print(global_max)
