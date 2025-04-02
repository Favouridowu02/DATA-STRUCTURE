#!/usr/bin/python3
"""
    This Module contains a function that contains the solution to Russian Doll Envelop Question

    Question:
    Given a string s, return the number of palindromic substrings in it.
    A string is a palindrome when it reads the same backward as forward.
    A substring is a contiguous sequence of characters within the string.

    Example 1:
    Input: s = "pqrp"
    Output: 4
    Explanation: Three palindromic strings: "p", "q", "r","p".
"""

def countSubstrings(s):
    """
        Recursive Approach
        This Function is used to find the number of palindromic substrings in a given string s

        Arguments:
            - s: a string
        Returns:
            - int: the number of palindromic substrings
        Space Complexity: O(n^2)
        Time Complexity: O(n^2)
    """
    n = len(s)
    dp = [[-1]*n for _ in range(n)]

    def helper(i, j):
        # base case
        if i == j:
            dp[i][j] = True
            return dp[i][j]
        if dp[i][j] != -1:
            return dp[i][j]

        # Recursive Case
        if s[i] == s[j] and (j == i+1 or helper(i+1, j-1)):
            

    helper(0, n-1)
    res = 0
    for l in range(1,n+1):
        for i in range(n-l+1):
            j = i+l -1
            if dp[i][j]: res += 1