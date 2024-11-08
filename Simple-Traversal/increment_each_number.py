def all_num(x):
    b = len(x)
    for i in range(b):
        x[i]+=1
        
x=[1,2,3]
all_num(x)
print(x, "should be [2,3,4]")
        
        
        