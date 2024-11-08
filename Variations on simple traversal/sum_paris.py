def print_sum_pairs(x,n):
    for i in range(len(x)):
        print(x[i] )
        for j in range(i, len(x)):
            print(x[j])
            if(x[i]+x[j] == n):
                print(i,j)
                

x = [2, 3, 4]
print_sum_pairs(x, 6)
print("Should print (0, 2), (1, 1)")
