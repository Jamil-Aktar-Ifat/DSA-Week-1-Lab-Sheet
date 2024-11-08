def add_prev(x,n):
    x[0]+=n
    for i in range(1,len(x)):
        x[i]+=x[i-1]
    
    

x = [4, -1, 2, -2, 3]
add_prev(x, -3)
print(x, "should be [1, 0, 2, 0, 3]")
