#!/usr/bin/python3

def diagonal_difference(arr):
    d1, d2 = 0,0
    for i in range(len(arr)):
        d1 += arr[i][i]
        d2 += arr[len(arr)-i-1][i]
    return abs(d1-d2)


ex_arr = [
        [11, 2, 4], 
        [4, 5, 6], 
        [10, 8, -12]
    ]
print(diagonal_difference(ex_arr))
