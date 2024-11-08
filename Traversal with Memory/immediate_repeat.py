def immed_reps(x):
    count = 0
    for i in range(1, len(x)):
        if(x[i] == x[i-1]):
            count+=1
    return count

x = [3, 3, 1, 4, 4, 1, 5, 5]
print(immed_reps(x), "should be 3")
