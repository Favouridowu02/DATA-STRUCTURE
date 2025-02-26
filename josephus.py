#!/usr/bin/python3
"""
    This Module contains a function that
    the winner the Josephus problem.
"""

def findTheWinner(n, k):
    """
        This function is used to find the Winner using
        Josephus Problem solving Method

        Arguments:
            n: The Total number of people in the circle
            k: The step Count number for elimination
    """
    # create an Array
    arr = [i + 1 for i in range(n)]
    def helper(arr, start_index):
        # base case
        if len(arr) == 1:
            return arr[0]
        # recursive case
        index_to_remove = (start_index + k - 1) % len(arr)
        del arr[index_to_remove]
        return helper(arr, index_to_remove)
        
    
    return helper(arr, 0)



# Alternatives

def findTheWinner_1(n, k):
    def josephus(n):
        if n == 1:
            return 0
        #recursive case
        return (josephus(n - 1) + k) % n
    return josephus(n) + 1