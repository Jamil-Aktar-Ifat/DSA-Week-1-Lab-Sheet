def my_sum(x):
    sum=0
    for i in range(0, len(x)):
        sum += x[i]
    return (sum)
    
x = [1, 2, -3]
print(my_sum(x), "should be 0")