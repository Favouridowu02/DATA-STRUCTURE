#!/usr/bin/python3
"""
    This Module contains a function for solving LongestChain pairs

    Question:
    
    Coding Exercise: Max Length of Pair Chain
    You are given an array of n pairs pairs where pairs[i] = [lefti, righti] and lefti < righti.

    A pair p2 = [c, d] follows a pair p1 = [a, b] if b < c. A chain of pairs can be formed in this fashion.

    Return the length longest chain which can be formed.

    You do not need to use up all the given intervals. You can select pairs in any order.



Example 1:

Input: pairs = [[2,3],[3,4],[4,5]]
Output: 2
Explanation: The longest chain is [2,3] -> [4,5].

"""

def findLongestChain(pairs):
    """
        The Tabulation or bottom up approach is applied
        This Function is used for solving LongestChain Problem

        Arguments:
            - pairs: a two dimensional Array. An array containing an array of length 2
        
        Return: the Lenght Longest Increasing Sequence of the Array
    """
    n = len(pairs)
    dp = [1]*n
    pairs.sort()
    longest_chain = 1

    for i in range(1, n):
        for j in range(i):
            if pairs[j][1] < pairs[i][0] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
        if dp[i] > longest_chain: longest_chain = dp[i]

    return longest_chain

