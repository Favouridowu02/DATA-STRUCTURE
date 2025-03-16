#!/usr/bin/env python3
"""
    This module contains a function that solves a dynamic programming Question using KnapSack

    Question 1: Target Sum: You are given an integer array nums and an integer target.
    You want to build an expression out of nums by adding one of the symbols '+' and '-'
    before each integer in nums and then concatenate all the integers.
    
    For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and
    concatenate them to build the expression "+2-1".
    Return the number of different expressions that you can build, which evaluates to target.
"""


def findTargetSumWays(nums, target):
    """
        This Function is used to solve the findTargetSumWays Questions

        Arguments:
            nums: An array of integers
            target: The target number
        
        Space Complexity: O(n)
        Time Complexity: O(2^n)
    """
    ways_number = 0
    n = len(nums)
    
    def helper(curr, index):
        nonlocal ways_number
        # Base case
        if len(curr) == n and sum(curr) == target:
            ways_number += 1
            return
        if len(curr) >= len(nums): return

        # Recursive Case
        # positive
        curr.append(nums[index])
        helper(curr, index + 1)
        curr.pop()
        
        # negative
        curr.append((-1 * nums[index]))
        helper(curr, index + 1)
        curr.pop()
        
    helper([], 0)
    return ways_number

# nums = [1,1,1,1]
# target = 2
# print(findTargetSumWays(nums, target))


def findTargetSumWays_1(nums, target):
    """
        This is the an Optimised Version
    """
    n = len(nums)
    summation = sum(nums)
    dp = [[None]*(2*summation+1) for _ in range(n)]

    def helper(index,sum_nums):
        #base case
        if index<0:
            if sum_nums==target:return 1
            else:return 0
        if dp[index][sum_nums+summation]!=None:return dp[index][sum_nums+summation]

        negative = helper(index-1,sum_nums+-1*nums[index])
        positive = helper(index-1,sum_nums+nums[index])    
        dp[index][sum_nums+summation] = negative+positive
        return dp[index][sum_nums+summation]
    return helper(n-1,0) 

"""
    Question 2:
    Partition Equal Subset Sum: Given an integer array nums,
    return true if you can partition the array into two subsets such that
    the sum of the elements in both subsets is equal or false otherwise.
"""
def canPartition(nums):
    n = len(nums)
    sum = 0
    for num in nums:
        sum+=num
    if sum%2 !=0: return False
    target =sum//2
    prev = [False]*(target+1) 
    curr = [False]*(target+1)
    prev[0]=True
    curr[0]=True

    for i in range(1,n+1):
        for j in range(1, target+1):
            #pick
            if nums[i-1]<=j:
                curr[j] = prev[j-nums[i-1]]
            else:
                curr[j] = False    
            #dontpick
            curr[j] = curr[j] or prev[j]
            
        prev = curr[:]  
    return curr[target]  