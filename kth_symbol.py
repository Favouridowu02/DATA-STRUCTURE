#!/usr/bin/python3
"""
    This Module contains a function that returns the Kth Symbol
    in the grammar sequence.
"""

def kth_symbol(n, k):
    """
        This function is designed to return the k=th symbol in the n-th row of
        the grammar sequence

        Arguments:
            n: The row number in the grammar sequence
            k: The position in the n-th row of the grammar sequence
    """
    #0
    #01 // THIS IS THE SEQUENCE
    #0110
    #01101001
    if n == 1: return 0
    length = 2 ** (n-1)
    half = length / 2
    if k <= half:
        return kth_symbol(n - 1, k)
    else:
        return int(not kth_symbol(n-1, k-half))
        # return 1 - kth_symbol(n-1, k-half)
