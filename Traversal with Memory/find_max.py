def my_max(x):
    maxNum =x[0]
    for i in range(len(x)):
        if x[i] > maxNum:
            maxNum = x[i]
    return maxNum
    
x = [1, 2, -3]
print(my_max(x), "should be 2")