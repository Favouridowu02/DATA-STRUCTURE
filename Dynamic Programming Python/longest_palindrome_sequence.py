#!/usr/bin/python3
"""
    This Module contains a function that contains the solution to Longest Palindromic Subsequence Question

    Question:
    Given a string s, find the longest palindromic subsequence's length in s.
    A subsequence is a sequence that can be derived from another sequence by deleting some or no elements
    without changing the order of the remaining elements.

    Example :
    Input: s = "cccacpc"
    Output: 5
    Explanation: One possible longest palindromic subsequence is "ccccc".
"""


def longestPalindromeSubseq(s):
    """
        Tabulation Approach
        This Function to find the longest palindromic subsequence in a string.

        Arguments:
            - s (str): The input string.
        Returns:
            - int: The length of the longest palindromic subsequence.
        Space Complexity: O(n^2)
        Time complexity: O(n^2)
    """
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    for l in range(1, n+1):
        for i in range(n-l+1):
            j = i + l - 1
            if i == j:
                dp[i][j] = 1
            elif s[i] == s[j]:
                dp[i][j] = 2 + dp[i+1][j-1]
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    return dp[0][n - 1]