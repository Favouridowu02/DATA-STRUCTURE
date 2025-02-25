#!/usr/bin/env python3
"""
    This Module contains a function monotonic_array

    Arguments:
        array - This is an Array of numbers

    Return: returns True if it is monotonic increasing or decreasing else False
"""


def monotonic_array(array):
    return_type = ""
    if len(array) in [0, 1]:
        return True
    for i in range(len(array) - 1):
        if array[i] == array[i + 1]:
            continue
        if array[i] > array[i + 1]:
            if return_type == "decreasing":
                return False
            return_type = "increasing"
        if array[i] < array[i + 1]:
            if return_type == "increasing":
                return False
            return_type = "decreasing"

    return True
