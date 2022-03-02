#!/usr/bin/python3

def birthdayCakeCandles(candles):
    max_arr = max(candles)
    return sum([x == max_arr for x in candles])

arr = [3, 2, 1, 3]
print(birthdayCakeCandles(arr))
