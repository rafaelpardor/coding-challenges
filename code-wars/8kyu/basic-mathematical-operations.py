#!/usr/bin/python3
# Challenge: codewars.com/kata/57356c55867b9b7a60000bd7/

def basic_op(operator, value1, value2):
    return eval("{}{}{}".format(value1, operator, value2))
