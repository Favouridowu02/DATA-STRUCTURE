#!/usr/bin/python3
"""
    This Module contains a Function tow that is used to solve the Tower of Hanoi 
    using Recursive function
"""

def toh(N, fromm, to, aux):
    """
        This is function that solves the Tower of Hanoi Problem Recursively

        Arguments:
            N - The number of disks to be moved from the source rod to the destination Rod
            fromm - The source rod from which the disks are to be moved
            to: The Destination rod to which the disks are to be moved
            aux: The helper rod for temporary holding of the disks
    """
    count=0
    def helper(N, fromm, to, aux):
        """ This Is am helper function for the recursive calls"""
        if N==1:
            nonlocal count
            print("move disk " + str(N) + " from rod " + str(fromm) + " to rod " + str(to))
            count += 1
            return
        helper(N - 1, fromm, aux, to)
        print("move disk " + str(N) + " from rod " + str(fromm) + " to rod " + str(to))
        count += 1
        helper(N - 1, aux, to, fromm)

    helper(N, fromm, to, aux)
    return count
        
