def sum_of_squares(L):
    total = 0 
    for i in L:
        total += i** 2 
    return total

sum_of_all = sum_of_squares([2,4,5,4])
print(sum_of_all)