#!/usr/bin/python3
"""
    This Module contains a function that contains the solution to Longest Palindromic Substring Question

    Question:
    Given a string s, return the longest  palindromic substring in s.
    A string is a palindrome when it reads the same backward as forward.
    A substring is a contiguous sequence of characters within the string.
    Example :

    Input: s = "pabad"
    Output: "aba"
"""


def longestPalindrome(s):
    """
        Tabulation Approach
        This Function is used to find the longest palindromic substring in a given string s

        Arguments:
            - s: a string
        Returns:
            - str: the longest palindromic substring
        Space Complexity: O(n^2)
        Time Complexity: O(n^2)
    """
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    longest = ''
    for l in range(1, n + 1):
        for i in range(n-l + 1):
            j = i + l - 1
            if i == j: 
                dp[i][j] =True
            elif s[i] == s[j] and (j == i + 1 or dp[i + 1][j - 1]):
                dp[i][j] = True
            else:
                dp[i][j] = False
            if dp[i][j]:
                longest = s[i:j+1]
    return longest