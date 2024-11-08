def int_every_third(x):
    for i in range(0,len(x),3):
        x[i]+=1
    
    
x = [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(x)
int_every_third(x)
print(x)