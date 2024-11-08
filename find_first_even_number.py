def find_first_even(x):
    for i in range(len(x)):
        if(x[i]%2==0):
            p=x[i]
            # print(i)
            print(f"first even number:{p} at position: {i}")
            return i
    
x=[1, 1, 1, 1, 2, 3, 4, 5]
find_first_even(x)
print(x)