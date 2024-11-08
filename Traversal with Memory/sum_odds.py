def odd_sum(x):
    sum = 0
    for i in range(len(x)):
        if(x[i]%2 ==1):
            sum+=x[i]
    return sum

x = [5, 2, -3, 0, 1]
print(odd_sum(x), "should be 3")