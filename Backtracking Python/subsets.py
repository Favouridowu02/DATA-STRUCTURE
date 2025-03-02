#!/usr/bin/python3
"""
    This Module contains a function power_set that solves the subsets using python

    Question:
    Power Set - Given an integer array of unique elements,
    return all possible subsets (the power set). The solution
    set must not contain duplicate subsets. Return the solution in any order.
"""

def power_set(nums):
    """
    """
    output = []
    def helper(nums, i , subset):
        if i == len(nums):
            output.append(subset.copy())
            return
        helper(nums, i +1, subset)
        subset.append(nums[i])
        helper(nums, i + 1, subset)
        subset.pop()
    
    helper(nums, 0, [])
    return output


# Testing 
print(power_set([1, 2, 4, 6]))




"""
Given an integer array nums that may contain duplicates, return all possible
subsets
(the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
Example: nums = [1,3,3]

Output = [[], [1], [3], [1,3], [3,3], [1,3,3]]
"""

def subsetsWithDup(nums):
    """
    """
    nums.sort()
    res = []
    def helper(i, curr):
        if i == len(nums):
            res.append(curr.copy())
            return
        # include
        curr.append(nums[i])
        helper(i + 1, curr)
        curr.pop() # back trcking step
        while i < len(nums) - 1 and nums[i] == nums[i+1]:
            i += 1
        helper(i + 1, curr)

        
    helper(0, [])
    return res