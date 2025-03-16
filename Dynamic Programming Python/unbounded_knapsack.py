#!/usr/bin/python3
"""
    This Module contains functions that are used to solve an unbounded knapsack problem

    Question:
    Given a set of N items, each with a weight and a value, represented by the
    array w and val respectively. Also, a knapsack with weight limit W.

    The task is to fill the knapsack in such a way that we can get the maximum profit.
    Return the maximum profit.

    Note: Each item can be taken any number of times.
    Input: N = 2 W = 3 val = [4, 2] wt = [3, 1]
    Output: 3
    Explanation: 
    1.Pick the 2nd element thrice.
    So, Total value = 2 + 2 + 2 = 6. and the total weight = 1 + 1 + 1  = 3 
which is <= 3.
"""


def knapSack(N, W, val, wt):
    """
        This is the Memoization approach
    """
    dp = [[-1]*(W+1) for _ in range(N+1)]
    
    for j in range(W+1):
        dp[0][j] = 0
    
    for i in range(N+1):
        dp[i][0] = 0
    
    for i in range(1,N+1):
        for j in range(1,W+1):
            exclude = dp[i-1][j]
            include = 0
            if wt[i-1] <=j:
                include = val[i-1] + dp[i][j -wt[i-1]]
            dp[i][j] = max(exclude,include)
    return dp[N][W]


def knapSack(N, W, val, wt):
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
    dp = [[0]*(W+1) for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, W+1):
            exclude = dp[i-1][j]
            include = 0
            if wt[i - 1] <= j:
                include = val[i-1] + dp[i][j - wt[i-1]]
            dp[i][j] = max(exclude, include)
    return dp[N][W]


def knapSack_1(N, W, val, wt):
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
    for i in range(1, N+1):
        for j in range(1, W+1):
            exclude = prev[j]
            include = 0
            if wt[i - 1] <= j:
                include = val[i-1] + curr[j - wt[i-1]]
            curr[j] = max(exclude, include)
        prev = curr.copy()
    return curr[W]