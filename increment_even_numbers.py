def inc_evens(x):
    for i in range(len(x)):
        if(x[i]%2==0):
            x[i]+=1
        else:
            x=x
    
    
    
x= [5,1,4,6,7]
inc_evens(x)
print(x)