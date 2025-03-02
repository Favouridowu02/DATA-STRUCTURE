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


def permuteUnique(nums):
    """
        This function is used to return the unique permute for each values in the arrays

        Arguments:
            nums - the array of integers
        
        Returns: A collection of all the unique possible permutation
    """
    result = []
    def helper(i):
        # Base case
        if i == len(nums) - 1:
            result.append(nums[:])
            return
        # Recursive case
        hash = {}
        for j in range(i, len(nums)):
            if nums[j] not in hash:
                hash[nums[j]]=True
                nums[i], nums[j] = nums[j], nums[i]
                helper(i + 1)
                nums[i], nums[j] = nums[j], nums[i]
    helper(0)
    return result