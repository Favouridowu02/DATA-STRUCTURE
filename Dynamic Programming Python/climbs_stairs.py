#!/usr/bin/python3
"""
    This module contains a function that solve the Climb Stairs Problem
"""

def climbStairs(n):
    if n<=2: return n
    def helper(first,second,n,curr):
        #subproblem
        #base condition
        next = first + second
        if curr==n: return next
        return helper(second,next,n,curr+1)
    return helper(1,2,n,3)