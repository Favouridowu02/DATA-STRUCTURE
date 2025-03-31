#!/usr/bin/python3
"""
    This Module contains a function that contains the solution to Russian Doll Envelop Question

    Question:
    Coding Exercise: Russian Doll Envelopes
    You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi] represents the width and the height of an envelope.
    One envelope can fit into another if and only if both the width and height of one envelope are greater than the other envelope's width and height.

    Return the maximum number of envelopes you can Russian doll (i.e., put one inside the other).
    Note: You cannot rotate an envelope.

    Example :
    Input: envelopes = [[6,5],[7,5],[7,8],[3,4]]
    Output: 3
    Explanation: The maximum number of envelopes you can Russian doll is 3 ([3,4] => [6,5] => [7,8]).
"""


def maxEnvelopes(envelopes):
    """
        Tabulation Approach is used
        This Function solves the question above
        Arguments:
            - envelopes: An Array containing an array of length 2. Each representing the [width, height]

        Return:  the maximum number of envelopes you can Russian doll

        Space Complexity: O(n)
        Time Complexity: O(n^2)
    """
    
    envelopes.sort(key = lambda x:(x[0], -x[1]))

    # LIS on height
    n = len(envelopes)
    dp = [1]*n
    maximum = 1

    for i in range(1, n):
        for j in range(i):
            if envelopes[i][1] > envelopes[j][1] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1

            if dp[i] > maximum: maximum = dp[i]
    return maximum


def maxEnvelopes_2(envelopes):
    """
        Binary Search Approach is used
        This Function solves the question above
        Arguments:
            - envelopes: An Array containing an array of length 2. Each representing the [width, height]

        Return:  the maximum number of envelopes you can Russian doll

        Space Complexity: O(n)
        Time Complexity: O(nlogn)
    """
    envelopes.sort(key = lambda x:(x[0],-x[1]))
 
    n = len(envelopes)
    sub = [envelopes[0][1]]
 
    def binary_search(sub,num):
        left, right = 0,len(sub)
        while left<right:
            mid = (left+right)//2
            if num>sub[mid]:
                left = mid+1
            else:
                right = mid
        return left
 
    for i in range(1,n):
        num = envelopes[i][1]
        if num>sub[-1]:
            sub.append(num)
        else:
            x = binary_search(sub,num)
            sub[x]=num
    return len(sub)