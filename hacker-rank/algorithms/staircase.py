#!/usr/bin/python3
import sys

def staircase(n):
    ret = []
    for i in range(1, n+1):
        ret.append(" "*(n-i)+"#"*i)
    sys.stdout.write('\n'.join(ret))

staircase(6)
