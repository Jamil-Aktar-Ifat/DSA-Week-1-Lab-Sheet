def records(x):
    
    high = x[0]
    count = 1
    for i in range(len(x)):
        if(x[i] > high):
            high = x[i]
            count+=1
    return count
    
    
x = [2, 3, 4, 3, 2, 1]
print(records(x), "should be 3")