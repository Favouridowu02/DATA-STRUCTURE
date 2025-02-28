#!/usr/bin/env python3
"""
    This module contains a function permute that uses backtracking
    to find the permutation
"""

def permute(nums):
    """
        This function is used to find the permutation of the array nums

        Argument:
            nums - an array of distinct integers
    """
    n = len(nums)
    result = []
    
    def helper(index):
        if index == n - 1:
            result.append(nums[:])
            return
        for j in range(index, n):
            nums[j],nums[index] = nums[index],nums[j]
            helper(index + 1)
            nums[j],nums[index] = nums[index],nums[j]
    helper(0)
    return result