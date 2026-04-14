#!/usr/bin/python3

"""
Description: Given a string s, find the length of the longest substring without duplicate characters.

Link: https://leetcode.com/problems/longest-substring-without-repeating-characters
"""

# Using set
def lengthOfLongestSubstring(s: str) -> int:
        test_list = []
        big_length = 0
        for i in list(s):
            # if i in test_list:
            while i in test_list:
                test_list.pop(0)
            test_list.append(i)
            big_length = max(len(test_list), big_length)            
        return big_length

# Using dictionary
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}  # Dictionary to store each character’s latest index
        left = 0  # Left pointer of the sliding window
        max_length = 0  # Track the maximum length found

        for right, char in enumerate(s):  # Iterate over the string with both index (right) and character
            if char in char_index and char_index[char] >= left:
                # If we see a repeat within the current window, move left pointer right past the previous occurrence
                left = char_index[char] + 1

            # Update the character’s latest index
            char_index[char] = right

            # Calculate the current window length and update max length if needed
            max_length = max(max_length, right - left + 1)

        return max_length

test = "aa"
print(lengthOfLongestSubstring(test))
