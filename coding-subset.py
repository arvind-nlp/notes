#https://stackoverflow.com/questions/29456502/subset-sum-with-backtracking-on-python

def twentyone(array, num=21):

    result=[]

    if num < 0:
        return result
    if len(array) == 0:
        if num == 0:
            result.append([])

        return result

        
    excluded = twentyone(array[1:], num)
    included = twentyone(array[1:], num - array[0])

    for solution in excluded:
        result.append( solution )
    for solution in included:
        result.append( [array[0]] + solution )

    return result

print(twentyone([5, 16, 3, 2]))