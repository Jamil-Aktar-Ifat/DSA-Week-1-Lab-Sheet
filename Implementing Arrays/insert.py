def my_insert(a,x,n,i):
    
     for j in range(n - 1, i - 1, -1):
         a[j + 1] = a[j]
         a[i] = x
    
a = [10, 20, 40, 50, 60, 0, 0, 0]
n = 5
x = 30
i = 2
my_insert(a, x, n, i)
print("Should move values 60, 50, 40 (in that order) into the next slot, and then put 30 at index 2")
print(a, "should now be [10, 20, 30, 40, 50, 60, 0, 0]")
print(len(a), "should still be 8")