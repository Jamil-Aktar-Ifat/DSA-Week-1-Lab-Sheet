def find_last_sixy(x):
    for i in range(len(x)-1, -1, -1):
        if("6" in str(x[i])):
            return i 
    return -1
    
x = [6, 8, 16, 18, 24]
n = find_last_sixy(x)
print(n, "should be 2")
print(x[n], "should be 16")
print(x, "should still be [6, 8, 16, 18, 24]")