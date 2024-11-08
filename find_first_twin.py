def find_first_twins(x):
    for i in range(len(x)-1):
        if(x[i] == x[i+1]):
            print(i)
            return i 
    print(-1) 
    return - 1      
    
x = [4, 4, 3, 3, 2]
n = find_first_twins(x)
print(n, "should be 0")
print(x[n], "should be 4")
print(x[n + 1], "should also be 4")