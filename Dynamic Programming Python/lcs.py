#!/usr/bin/python3
"""
    This Module contains contains the solution to Longest Common Subsequence Problems

    Question:
    Coding Exercise: LCS ( Longest Common Subsequence)
    Given two strings text1 and text2, return the length of their longest common subsequence.
    If there is no common subsequence, return 0.
    A subsequence of a string is a new string generated from the original string with some
    characters (can be none) deleted without changing the relative order of the remaining characters.

    •For example, "ace" is a subsequence of "abcde".
    A common subsequence of two strings is a subsequence that is common to both strings.
    Example: 
    Input: text1 = "pbcdq", text2 = "pcq" 
    Output: 3  
    Explanation: The longest common subsequence is "pcq" and its length is 3.
"""


def longestCommonSubsequence(text1, text2):
    """
        Recursive Approach
        This Function solve the longest Common Subsequence Problem

        Arguments:
            - text1: A String
            - text2: A String
        Space Complexity: O(n + m)
        Time Complexity: O(2^(n + m))
    """
    n = len(text1)
    m = len(text2)

    def helper(index1, index2):
        # Base case
        if index1 > n - 1 or index2 > m - 1:
            return 0
    
        # Recursive Case
        # Equal
        if text1[index1] == text2[index2]:
            return 1 + helper(index1 + 1, index2 + 1)
        # Not Equal
        return max(helper(index1 + 1, index2), helper(index1, index2 + 1)) 
    return helper(0, 0)


def longestCommonSubsequence_2(text1, text2):
    """
        Memoization Approach
        This Function solve the longest Common Subsequence Problem

        Arguments:
            - text1: A String
            - text2: A String
        Space Complexity: O(n * m)[Table] + O(n + m)[Recursive Call Stack] == O(n * m)
        Time Complexity: O((n * m))
    """
    n = len(text1)
    m = len(text2)
    dp = [[-1]*m for _ in range(n)]

    def helper(index1, index2):
        # Base case
        if index1 > n - 1 or index2 > m - 1:
            return 0
        if dp[index1][index2] != -1: return dp[index1][index2]
        # Recursive Case
        # Equal
        if text1[index1] == text2[index2]:
            dp[index1][index2] = 1 + helper(index1 + 1, index2 + 1)
            return dp[index1][index2]
        # Not Equal
        dp[index1][index2] = max(helper(index1 + 1, index2), helper(index1, index2 + 1)) 
        return dp[index1][index2]
    return helper(0, 0)


def longestCommonSubsequence_3(text1, text2):
    """
        Tabulation Approach
        This Function solve the longest Common Subsequence Problem

        Arguments:
            - text1: A String
            - text2: A String
        Space Complexity: O(n * m) [Table Size]
        Time Complexity: O(n * m)
    """
    n = len(text1)
    m = len(text2)
    dp = [[0]*(m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if text1[i] == text2[j]:
                dp[i][j] = 1 + dp[i-1][j - 1]
            else:
                dp[i][j] = max(dp[i -1][j], dp[i][j - 1])

    return dp[n][m]


def longestCommonSubsequence_3(text1, text2):
    """
        Space Optimised Tabulation Approach
        This Function solve the longest Common Subsequence Problem

        Arguments:
            - text1: A String
            - text2: A String
        Space Complexity: O(min(n, m))
        Time Complexity: O(n * m)
    """
    n = len(text1)
    m = len(text2)
    prev = [0]*(m+1)
    curr = [0]*(m+1)

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if text1[i] == text2[j]:
                curr[j] = 1 + prev[j - 1]
            else:
                curr[j] = max(prev[j], curr[j - 1])
        prev = curr[:]
    return curr[m]
