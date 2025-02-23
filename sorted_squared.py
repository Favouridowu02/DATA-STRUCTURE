#!/usr/bin/python3
"""
    This Module contains the Sorted Squared

Question:
    You are given an array of Integers in which
    each subsequent value is not less than the
    previous value. Write a function that takes
    this array as an input and returns a new array
    with the squares of each number sorted in ascending order.
"""


def sorted_squared(array):
    """
        This function is used to sort the squares of the
        given array in ascending order.
        Args:
            array: List of Integers
        Returns:
            List of Integers
    """
    array = [ i**2 for i in array]
    array.sort()
    return array