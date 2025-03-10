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
    """
        This Function used to find the sum

        Arguments:
            candidates: An array of numbers containing the candidatrees
            target: an Integer.

        Space Complexity: S = O(T/M)
        Time Complexity: T = O(N^(T/M + 1))

        Where N - no of candidates
              T - target
              M - minimum value among candidates
    """
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


# Alternatives
def combinationSum_1(candidates, target):
    res =[]
    n = len(candidates)
    def helper(start_index, curr, sum_included):
        if sum_included > target:
            return
        if (sum_included == target):
            res.append(curr[:])

        for j in range(start_index, n):
            curr.append(candidates[j])
            helper(j, curr, sum_included + candidates[j])
            curr.pop()

    helper(0, [], 0)
    return res 


def combinationSum2(candidates, target):
    """
        This Function is used to find the combination

        Arguments:
            candidates: An array of integers
            target: An Integer

        Space Complexity: S - O(n)
        Time Complexity: T - O(2^n)

        Question: 
        Given a collection of candidate numbers (candidates) and a target number
        (target), find all unique combinations in candidates where the
        candidate numbers sum to target.

        Each number in candidates may only be used once in the combination.
        Note: The solution set must not contain duplicate combinations.
    """
    candidates.sort()
    res = []
    n = len(candidates)
    def helper(index, curr, curr_sum):
        # Base case
        if curr_sum == target:
            res.append(curr[:])
            return
        if curr_sum > target:
            return
        if index > n - 1:
            return
        # Recursive case
        hash = {}
        for i in range(index, n):
            if candidates[i] not in hash:
                hash[candidates[i]] = True
                curr.append(candidates[i])
                helper(i + 1, curr, curr_sum + candidates[i])
                curr.pop() # Back Tracking step


    helper(0, [], 0)
    return res



def combinationSum3(k, n):
    """
        This Function is used to find the combination

        Arguments:
            candidates: An array of integers
            target: An Integer

        Space Complexity: S - O(n)
        Time Complexity: T - O(2^n)

        Question:
        Find all valid combinations of k numbers that sum up to n such that
        the following conditions are true: Only numbers 1 through 9 are used.
        Each number is used at most once.
        Return a list of all possible valid combinations.The list must not
        contain the same combination twice, and the combinations may be returned in any order.
    """
    res = []
    def backtrack(number,curr,currSum):
        if currSum ==n and len(curr)==k:
            res.append(curr[:])
            return
        if currSum >n or len(curr)==k:
            return
        for x in range(number,10):
            curr.append(x)
            backtrack(x+1,curr,currSum+x)
            curr.pop()
    backtrack(1,[],0)
    return res
