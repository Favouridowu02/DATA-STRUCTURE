#!/usr/bin/env python3
"""
    This Module contains a function that solve the Palindrom question 2

    Question:  

"""


def minCut(s):
    """
        Pruned Recursion Approach    
        This function calculates the minimum number of cuts needed to partition a string into palindromic substrings.

        Finds the minimum number of cuts needed to partition a given string `s` 
        such that every substring of the partition is a palindrome.

        Arguments:
            s (str): The input string to be partitioned.

        Returns:
            int: The minimum number of cuts required to partition the string 
            into palindromic substrings.
        Space Complexity: O(n^2)
        Time Complexity: O(n^3)
    """
    n = len(s)
    def isPalindrome(i, j):
        """
            Helper function to check if a substring of `s` is a palindrome.
            
            Arguments:
                i: The starting Index
                j: The ending Index
        """
        while i < j:
            if s[i]!=s[j]: return False
            i += 1
            j -= 1
        return True

    def partitions(start, end):
        # Base case
        if start == end or isPalindrome(start, end):
            return 0

        # Recursive Case
        minimum = end - start
        for end_index in range(start, end):
            if isPalindrome(start, end):
                minimum = min(minimum, 1 + partitions(end_index + 1, end))

        return minimum  
        
    return partitions(0, n-1)


def minCut_1(s):
    """
        Memoization Approach    
        This function calculates the minimum number of cuts needed to partition a string into palindromic substrings.

        Finds the minimum number of cuts needed to partition a given string `s` 
        such that every substring of the partition is a palindrome.

        Arguments:
            s (str): The input string to be partitioned.

        Returns:
            int: The minimum number of cuts required to partition the string 
            into palindromic substrings.
        Space Complexity: O(n^2)
        Time Complexity: O(n^3)
    """
    n = len(s)
    isPalindrome = [[0] for _ in range(n)]  
    for l in range(1, n+1):
        for i in range(n-l+1):
            j = i + l - 1
            i == j
            if i == j: isPalindrome[i][j] = True
            elif s[i] == s[j] and (j == i +1 or isPalindrome[i+1][j-1]):
                isPalindrome[i][j] = True
            else:
                isPalindrome[i][j] = False

    dp = [[None] * n for _ in range(n)]
    def partitions(start, end):
        # Base case
        if start == end or isPalindrome[start][end]:
            return 0

        # Recursive Case
        if dp[start][end] is not None:
            return dp[start][end]
        minimum = end - start
        for end_index in range(start, end):
            if isPalindrome[start][end]:
                minimum = min(minimum, 1 + partitions(end_index + 1, end))
        dp[start][end] = minimum
        return dp[start][end]
        
    return partitions(0, n-1)


def minCut_2(s):
    """
        Tabulation Approach
        This function calculates the minimum number of cuts needed to partition a string into palindromic substrings.

        Finds the minimum number of cuts needed to partition a given string `s` 
        such that every substring of the partition is a palindrome.

        Arguments:
            s (str): The input string to be partitioned.

        Returns:
            int: The minimum number of cuts required to partition the string 
            into palindromic substrings.

        Space Complexity: O(n^2)
        Time Complexity: O(n^3)
    """
    n = len(s)
    dp = [[0]*n for _ in range(n)]

    for l in range(1, n+1):
        for i in range(n-l+1):
            j = i + l - 1
            if i == j:
                dp[i][j] = 0
            elif s[i] == s[j] and (j == i + 1 or dp[i+1][j-1] == 0):
                dp[i][j] = 0
            else:
                dp[i][j] = float('inf')
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + 1) 

    return dp[0][n-1]


def minCut(s):
    """
        Space Optimization Approach - Tabulation
        This function calculates the minimum number of cuts needed to partition a string into palindromic substrings.

        Finds the minimum number of cuts needed to partition a given string `s` 
        such that every substring of the partition is a palindrome.

        Arguments:
            s (str): The input string to be partitioned.

        Returns:
            int: The minimum number of cuts required to partition the string 
            into palindromic substrings.
        Space Complexity: O(n^2)
        Time Complexity: O(n^2)

    """
    n = len(s)
    isPalindrome = [[False]*n for _ in range(n)]
    for l in range(1, n+1):
        for i in range(n-l+1):
            j = i + l - 1
            if i == j:
                isPalindrome[i][j] = True
            elif s[i] == s[j] and (j == i + 1 or isPalindrome[i+1][j-1]):
                isPalindrome[i][j] = True
            else:
                isPalindrome[i][j] = False
    dp = [0] * n
    for end in range(n):
        min_cuts = end
        for start in range(end + 1):
            if isPalindrome[start][end]:
                min_cuts = 0 if start == 0 else min(min_cuts, dp[start - 1] + 1)
        dp[end] = min_cuts
    return dp[n - 1]