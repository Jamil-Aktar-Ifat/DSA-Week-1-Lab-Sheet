def max_count(x):
    count = 0
    maxNum = x[0]
    for i in range(len(x)):
        if(x[i] >  maxNum):
            maxNum = x[i]
    for j in range(len(x)):
        if(x[j] == maxNum):
            count+=1
            
    return count
    
x = [5, 1, 5, 2, 5]
print(max_count(x), "should be 3")