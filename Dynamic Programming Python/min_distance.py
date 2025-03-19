#!/usr/bin/python3
"""
    This Module contains the solutions to Min Distance Problem of two strings

    Questions:

"""


def minDistance(word1, word2):
    """
        Recursive Solution
        This Function solves the Min Distance Problem

        Arguments:
            - word1:
            - word2: 
        Space Complexity: O(n * m)
        Time Complexity: O(n * m)
    """
    n = len(word1)
    m = len(word2)

    dp = [[-1]*m for _ in range(n)]

    def helper(index1, index2):
        # base case
        if index1 > n - 1 or index2 > m - 1:
            return 0
        if index1 > n - 1:
            return m - index2
        if index2 > m - 1:
            return n - index1

        if dp[index1][index2] != -1:
            return dp[index1][index2]
        # recursive Case
        if word1[index1] == word2[index2]:
            dp[index1][index2] = helper(index1 + 1, index2 + 1)
        else:
            replace = helper(index1 + 1, index2 + 1) + 1
            delete = helper(index1 + 1, index2) + 1
            insert = helper(index1, index2 + 1) + 1
            dp[index1][index2] = min(replace, delete, insert)
        return dp[index1][index2]
    return helper(0, 0)


def minDistance_1(word1, word2):
    """
        Memoization Approach
        This Function solves the Min Distance Problem

        Arguments:
            - word1:
            - word2:
        Space Complexity: O(m * n) 
        Time Complexity: O(m * n)
    """
    n = len(word1)
    m = len(word2)

    def helper(index1, index2):
        # base case
        if index1 > n - 1 or index2 > m - 1:
            return 0
        if index1 > n - 1:
            return m - index2
        if index2 > m - 1:
            return n - index1

        # recursive Case
        if word1[index1] == word2[index2]:
            return helper(index1 + 1, index2 + 1)
        replace = helper(index1 + 1, index2 + 1) + 1
        delete = helper(index1 + 1, index2) + 1
        insert = helper(index1, index2 + 1) + 1
        return min(replace, delete, insert)
    return helper(0, 0)


def minDistance_2(word1, word2):
    """
        Tabulation Approach
        This Function solves the Min Distance Problem

        Arguments:
            - word1:
            - word2: 
        Space Complexity: O(m * n) 
        Time Complexity: O(m * n)
    """
    n = len(word1)
    m = len(word2)
    dp = [[0]*(m+1) for _ in range(n +1)]

    for i in range(1, n + 1):
        dp[i][0] = i
        
    for j in range(1, m + 1):
        dp[0][j] = j

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                replace = dp[i - 1][j - 1] + 1
                delete = dp[i - 1][j] + 1
                insert = dp[i][j - 1] + 1
                dp[i][j] = min(replace, delete, insert)
    return dp[n][m]


def minDistance_3(word1, word2):
    """
        Space Optimised Tabulation Approach
        This Function solves the Min Distance Problem

        Arguments:
            - word1:
            - word2: 
        Space Complexity: O(min(m, n)) 
        Time Complexity: O(m * n)
    """
    n = len(word1)
    m = len(word2)
    prev = [0]*(m+1)
    curr = [0]*(m+1)

        
    for j in range(1, m + 1):
        prev[j] = j

    for i in range(1, n + 1):
        curr[0] = i
        for j in range(1, m + 1):
            if word1[i - 1] == word2[j - 1]:
                curr[j] = prev[j - 1]
            else:
                replace = prev[j - 1] + 1
                delete = prev[j] + 1
                insert = curr[j - 1] + 1
                curr[j] = min(replace, delete, insert)
        prev = curr[:]
    return prev[m]