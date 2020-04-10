#from g4g

def cutRod(price, n): 
    val = [0 for x in range(n+1)] 
  
    # Build the table val[] in bottom up manner and return 
    # the last entry from the table 
    for i in range(1, n+1): 
        max_val = 0 
        for j in range(1,i): 
             max_val = max(max_val, price[j] + val[i-j]) 
        val[i] = max_val 
  
    return val[n] 

# Driver program to test above functions 
arr = [0,1, 5, 8, 9, 10, 17, 17, 20] 
size = len(arr) 
print("Maximum Obtainable Value is " + str(cutRod(arr, size))) 
  
