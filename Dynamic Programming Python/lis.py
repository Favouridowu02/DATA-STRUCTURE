#!/usr/bin/python3
"""
    This Module contains contains the solution to Longest Increasing Subsequence Problems

    Question:
"""


def lengthOfLIS(nums):
    """
        Recursive Approach
        This Function solve the longest Increasing Subsequence Problem

        Arguments:
            - nums: An array of integers
        Space Complexity: O(n)
        Time Complexity: O(2^(n))
    """
    n = len(nums)

    def helper(curr_index, prev_index):
        # base case
        if curr_index > n - 1:
            return 0

        # Recursive Case
        exclude = helper(curr_index + 1, prev_index)
        include = 0
        if prev_index == -1 or nums[curr_index] > nums[prev_index]:
            include = 1 + helper(curr_index + 1, curr_index)
        return max(include, exclude)

    return helper(0, -1)


def lengthOfLIS_1(nums):
    """
        Memoization Approach
        This Function solve the longest Increasing Subsequence Problem

        Arguments:
            - nums: An array of integers
        Space Complexity: O(n^2)
        Time Complexity: O(n^2)
    """
    n = len(nums)
    dp = [[-1]*n for _ in range(n)]

    def helper(curr_index, prev_index):
        # base case
        if curr_index > n - 1:
            return 0

        if dp[curr_index][prev_index+1] != -1:
            return dp[curr_index][prev_index + 1]

        # Recursive Case
        exclude = helper(curr_index + 1, prev_index)
        include = 0
        if prev_index == -1 or nums[curr_index] > nums[prev_index]:
            include = 1 + helper(curr_index + 1, curr_index)
        dp[curr_index][prev_index+1] = max(include, exclude)
        return dp[curr_index][prev_index+1]

    return helper(0, -1)


def lengthOfLIS_2(nums):
    """
        Tabulation Approach or Bottom Up Approach
        This Function solve the longest Increasing Subsequence Problem

        Arguments:
            - nums: An array of integers
        Space Complexity: O(n^2)
        Time Complexity: O(n^2)
    """
    n = len(nums)
    dp = [[0]*(n+1) for _ in range(n+1)]

    for i in range(n-1, -1, -1):
        for j in range(i, -1, -1):
            exclude = dp[i+1][j]
            include = 0
            if j-1 == -1 or nums[i]>nums[j-1]:
                include = 1 + dp[i+1][i+1]
            dp[i][j] = max(exclude, include)
    return dp[0][0]


def lengthOfLIS_3(nums):
    """
        Tabulation Approach or Bottom Up Approach Using 1Dimensional Array
        This Function solve the longest Increasing Subsequence Problem

        Arguments:
            - nums: An array of integers
        Space Complexity: O(n)
        Time Complexity: O(n^2)
    """
    n = len(nums)
    dp = [1]*(n)

    max = 1
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j] and dp[j] +  1 > dp[i]:
                dp[i] = dp[j + 1]
        if dp[i]> max: max=dp[i]

    return max


def lengthOfLIS_4(nums):
    """
        Binary Search Approach
        This Function solve the longest Increasing Subsequence Problem

        Arguments:
            - nums: An array of integers
        Space Complexity: O(nlogn)
        Time Complexity: O(n)
    """
    def binarysearch(sub, num):
        left, right = 0, len(sub) - 1
        while left<right:
            mid = (left+right)//2
            if sub[mid] < num:
                left = mid + 1
            else:
                right = mid
        return left

    sub = [nums[0]]
    n = len(nums)

    for num in nums[1:]:
        if num>sub[-1]:
            sub.append(num)
        else:
            index = binarysearch(sub, num)
            sub[index] = num
    return 