#!/usr/bin/python3

def plus_minos(arr):
    pos = sum(map(lambda x: x > 0, arr))*1.0/len(arr)
    neg = sum(map(lambda x: x < 0, arr))*1.0/len(arr)
    zer = sum(map(lambda x: x == 0, arr))*1.0/len(arr)

    return "%f\n%f\n%f" % (pos,neg,zer)

ex_arr = [-4, 3, -9, 0, 4, 1]
print(plus_minos(ex_arr))
