def alt_sums(x):
    sum_even_indices = 0
    sum_odd_indices = 0
    for i in range(len(x)):
        if (i%2==0):
            sum_even_indices+=x[i]
        else:
            sum_odd_indices+=x[i]
    
    return [sum_even_indices, sum_odd_indices]     
    
    
x = [1, -1, 1, -1, 1, -1]
y = alt_sums(x)
print(y, "should be [3, -3]")