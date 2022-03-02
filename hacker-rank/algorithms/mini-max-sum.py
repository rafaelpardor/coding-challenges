#!/usr/bin/python3

def mini_max_sum(arr):
    arr_total = [sum(arr) - arr[i] for i in range(len(arr))]
    return min(arr_total), max(arr_total)

arr = [1, 2, 3, 4, 5]
print(mini_max_sum(arr))
