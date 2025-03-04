#!/usr/bin/python3
"""
    This module contains a function combination Sum

    Question:
    Given an array of distinct integers candidates and a target
    integer target, return a list of all unique combinations of
    candidates where the chosen numbers sum to target. You may
    return the combinations in any order.

    The same number may be chosen from candidates an unlimited number
    of times. Two combinations are unique if the frequency of at least
    one of the chosen numbers is different.

    (the integers in the candidates array are all non negative )

    Example:
        Input: candidates = [2,3,8,9], target = 9
        Output: [[2,2,2,3],[3,3,3],[9]]
"""
def combinationSum(candidates, target):
    #write code here
    #the integers in the candidates array are all non negative  
    res = []
    def helper(i, curr, total):
        # Base case
        if total == target:
            res.append(curr.copy())
            return
        if total > target or i >= len(candidates):
            return
        
        # Without incrementing
        curr.append(candidates[i])
        helper(i, curr, total + candidates[i])
        curr.pop()
        
        # with incrementing
        helper(i + 1, curr, total)
        
    helper(0, [], 0)
    return res
    
a = [2, 3, 8, 9]
target = 9

print(combinationSum(a, target))