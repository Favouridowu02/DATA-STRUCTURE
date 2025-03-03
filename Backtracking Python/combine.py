#!/usr/bin/python3
"""
    This Module contains a function to solve the combination using Backtracking

    Question:
    Given two integers n and k, return all possible combinations of k numbers
    chosen from the range [1, n]. You may return the answer in any order
"""


def combine(n, k):
    """
        This Function is used to find the combination of 1 - n with len of k
        
        Argument:
            n -
            k -
    """
    res = []
    def helper(start, curr):
        if len(curr) == k:
            res.append(curr.copy())
            return
        need = k - len(curr)
        for j in range(start, n - (need -1) + 1):
            curr.append(j)
            helper(j + 1, curr)
            curr.pop()
    
    helper(1, [])
    return res

