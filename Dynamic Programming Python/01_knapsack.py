#!/usr/bin/python3
"""
    This module contains a function knapSack that solve 

    Question:
    Coding Exercise: 01 Knapsack
    You are provided with a set of N items, each with a specified weight and value.
    Your objective is to pack these items into a backpack with a weight limit of W,
    maximizing the total value of items in the backpack. Specifically, you have two
    arrays: val[0..N-1], representing the values of the items, and wt[0..N-1], indicating
    their weights. Additionally, you have a weight limit W for the backpack.
    The challenge is to determine the most valuable combination of items where the
    total weight does not exceed W. Note that each item is unique and indivisible,
    meaning it must be either taken as a whole or left entirely.

    Input: N = 3 W = 8 values[] = [2,3,9] weight[] = [8,2,5]
    Output: 12
    Explanation: Choose the last 2 items that weighs 2 and 5 units respectively and
    hold values 3 and 9 that add up to 12. 

"""

def knapSack(W, wt, val, n):
    """
        This is the Recursion approach        
        Arguments:
            W: The weight constraint
            wt: An array of the weight of individual elements
            val: An array of the value of individual elements
            n: The length of the array
        
        Space Complexity; O(n)
        Time Complexity: O(2^n)
    """

    def helper(index, rem_weight):
        """
            Arguments:
                index: This represents the Array index
                rem_weight: This represents the remaining weight
        """
        # base case
        if index > n-1 and rem_weight == 0:
            return 0

        # recursive case
        exclude = helper(index + 1, rem_weight)
        include = 0
        if wt[index] <= rem_weight:
            include = val[index] + helper(index + 1, rem_weight - wt[index])

        return max(include, exclude)
    return helper(0, W)


def knapSack_2(W, wt, val, n):
    """
        This is the Memoization approach
        Arguments:
            W: The weight constraint
            wt: An array of the weight of individual elements
            val: An array of the value of individual elements
            n: The length of the array
        
        Space Complexity: O(n*W)
        Time Complexity: O(n*W)
    """
    dp = [[-1]*(W+1) for _ in range(n)]

    def helper(index, rem_weight):
        """
            Arguments:
                index: This represents the Array index
                rem_weight: This represents the remaining weight
        """
        # base case
        if index > n-1 and rem_weight == 0:
            return 0
        if dp[index][rem_weight] != -1:
            return dp[index][rem_weight]
        # recursive case
        exclude = helper(index + 1, rem_weight)
        include = 0
        if wt[index] <= rem_weight:
            include = val[index] + helper(index + 1, rem_weight - wt[index])

        dp[index][rem_weight] = max(include, exclude) # storing
        return dp[index][rem_weight]
    return helper(0, W)


def knapSack_3(W, wt, val, n):
    """
        This is the tabulation approach
        Arguments:
            W: The weight constraint
            wt: An array of the weight of individual elements
            val: An array of the value of individual elements
            n: The length of the array
        
        Space Complexity: O(n*W)
        Time Complexity: O(n*W)
    """
    dp = [[0]*(W+1) for _ in range(n + 1)]

    for i in range(1, n+1):
        for j in range(1, W+1):
            exclude = dp[i - 1][j]
            include = 0
            if wt[i-1]<= j:
                include = val[i-1] + dp[i-1][j-wt[i-1]]
            dp[i][j] = max(exclude, include)
    return dp[n][W]


def knapSack_4(W, wt, val, n):
    """
        This is the Space optimised tabulation approach
        Arguments:
            W: The weight constraint
            wt: An array of the weight of individual elements
            val: An array of the value of individual elements
            n: The length of the array
        
        Space Complexity: O(W)
        Time Complexity: O(n*W)
    """
    prev = [0]*(W+1)
    curr = [0]*(W+1)

    for i in range(1, n+1):
        for j in range(1, W+1):
            exclude = prev[j]
            include = 0
            if wt[i-1]<= j:
                include = val[i-1] + prev[j-wt[i-1]]
            curr[j] = max(exclude, include)
        prev = curr.copy()
    return curr[W]