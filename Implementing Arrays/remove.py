def my_remove(a,n,i):
    for j in range(i, n-1):
        a[j]  = a[j+1]
    a[n-1] = 0
    
    print("Value", a[j], "copied from index", j, "to", j - 1)

a = [1, 2, 3, 4, 5, 6, 7, 0]
n = 7
i = 0
my_remove(a, n, i)
print("Should move each entry from 7 down to 2, into the previous slot, and then put 0 at index 6")
print(a, "should now be [2, 3, 4, 5, 6, 7, 0, 0]")
print(len(a), "should still be 8")