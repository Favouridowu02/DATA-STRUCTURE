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

# This is an optimaised version of the sorted_squared method
# Time = 0(n) Space = 0(n)
def sorted_squared_array(array):
    """
        This function is used to sort the squares of the
        given array in ascending order.
        Args:
            array: List of Integers
        Returns:
           List of Integers
    """
    new_array = [0]*len(array)
    left_pointer = 0
    right_pointer = len(array) - 1
    
    for i in reversed(range(len(array))):
        left_squared = array[left_pointer] ** 2
        right_squared = array[right_pointer] ** 2

        if left_squared > right_squared:
            new_array[i] = left_squared
            left_pointer += 1
        else:
            new_array[i] = right_squared
            right_pointer -= 1
    return new_array

print(sorted_squared_array([-6, -3, 0, 8, 9]))