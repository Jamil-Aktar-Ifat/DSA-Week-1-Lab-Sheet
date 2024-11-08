def print_peaks(x):
    for i in range(1, len(x)-1):
        if(x[i-1] < x[i] and x[i] > x[i+1]):
            print(i)
            
    
    
x  = [1, 2, 1, 2, 1, 2, 1]
print_peaks(x)
print("Should print 1, 3, and 5")