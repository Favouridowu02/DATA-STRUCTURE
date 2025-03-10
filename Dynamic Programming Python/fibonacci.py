#!/usr/bin/python3
"""
    This Module contains a function that solve Fibonacci Series 
"""

def fibonacci(n):
    """
        This Function solves the Fibonacci series
        
        Arguments:
            - n: This is the argument that is passed to the function

        Space Complexity: O(n)
        Time Complexity: O(2^n)
        Return the Value of the Fibonacci series
    """
    if n <= 1:
        return n
    else: return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_2(n, ht={0:0, 1:1}):
    """
        This Function solves the Fibonacci series using Memoization
        
        Arguments:
            - n: This is the argument that is passed to the function
            - ht: this is an hash table that is used to store the memoized values

        Space Complexity: O(n)
        Time Complexity: O(n)
        Return the Value of the Fibonacci series
    """
    if n in ht:
        return ht[n]
    else:
        ht[n]  = fibonacci_2(n-1, ht) + fibonacci_2(n-2, ht)
        return ht[n]

def fibonacci_3(n):
    """
        This Function solves the Fibonacci series using Tabulation Approach
        
        Arguments:
            - n: This is the argument that is passed to the function

        Space Complexity: O(n)
        Time Complexity: O(n)
        Return the Value of the Fibonacci series
    """
    dp = [0]*(n+1)

    if n>0:
        dp[1] = 1
    count = 1
    while(count < n):
        count += 1
        dp[count] = dp[count - 1] + dp[count - 2]
    return dp[n]
    
def fibonacci_4(n):
    """
        This Function solves the Fibonacci series using Tabulation Approach
        
        Arguments:
            - n: This is the argument that is passed to the function

        Space Complexity: O(1)
        Time Complexity: O(n)
        Return the Value of the Fibonacci series
    """
    if n <= 1: return
    prev = 0
    curr = 1
    counter = 1
    while counter < n:
        next = prev + curr
        counter += 1
        prev = curr
        curr = next
    return curr