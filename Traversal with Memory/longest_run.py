def longest_run(x):
    longest_run = 1
    current_run = 1
    for i in range(1, len(x)):
        if(x[i] == x[i-1] ):
            current_run+=1
        else:
            current_run = 1
            
        if current_run > longest_run:
            longest_run = current_run
            
    return longest_run
    
    
x = [5]
print(longest_run(x), "should be 1")