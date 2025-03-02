#!/usr/bin/python3
"""
    This Module contains a Function tow that is used to solve the Power Sum
    using Recursive function
"""

def power_sum(array, power=1):
    """
    """
    sum = 0
    for i in array:
        if type(i) == list:
            sum += power_sum(i, power+1)
        else:
            sum += i
    return sum ** power