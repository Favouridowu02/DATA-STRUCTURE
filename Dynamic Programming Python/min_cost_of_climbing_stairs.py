"""
    Coding Exercise: Minimum Cost Climbing Stairs
    You are given an integer array cost where cost[i] is the cost of ith step on a staircase.
    Once you pay the cost, you can either climb one or two steps.
    You can either start from the step with index 0, or the step with index 1.

    Return the minimum cost to reach the top of the floor.

    Example 1:
    Input: cost = [10,20,30]
    Output: 20
    Explanation: You will start at index 1.
    - Pay 20 and climb two steps
"""

def minCostClimbingStairs(cost):
    """
        This Function Finds the minimum cost of climbing the stairs
        RECURSION APPROACH
        Arguments:
            - cost: an array of costs for each step
        Space complexity: O(n)
        Time complexity: O(n^2)
    """
    n = len(cost)
    def helper(index):
        # Returns the cost of reaching the top starting from step - index
        # Base Case
        if (index > n - 1): return 0
         
        # Recursive case
        # one step
        onestep = cost[index] + helper(index + 1)

        # two steps
        twostep = cost[index] + helper(index + 2)

        return min(onestep, twostep)
    return min(helper(0), helper(1))

def minCostClimbingStairs_2(cost):
    """
        This Function Finds the minimum cost of climbing the stairs
        MEMOIZATION APPROACH
        Arguments:
            - cost: an array of costs for each step
        Space complexity: O(n)
        Time complexity: O(n)
    """

    n = len(cost)
    mincost = [-1]

    def helper(index):
        # base case
        if index > n - 1: return 0

        # recursive case
        if mincost[index] != -1:
            pass

        # one step
        onestep = cost[index] + helper(index + 1)
        # two step
        twostep = cost[index] + helper(index + 2)
        mincost[index] = min(onestep, steptwo)
        return mincost[index]
    return min(helper(0), helper(1))

def minCostClimbingStairs_3(cost):
    """
        This Function Finds the minimum cost of climbing the stairs
        TABULATION APPROACH
        Arguments:
            - cost: an array of costs for each step
        Space complexity: O(n)
        Time complexity: O(n)
    """
    n = len(cost)
    mincost = [0]*(n+1)
    mincost[0] = 0
    mincost[1] = 0
    for i in range(2, n + 1):
        onestep = cost[i - 1] + mincost[i - 1]
        twostep = cost[i - 2] + mincost[i - 2]
        mincost[i] = min(onestep, twostep)
    return mincost[n]