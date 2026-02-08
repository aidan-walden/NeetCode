#
# Problem: Valid Palindrome
# Difficulty: Easy
# URL: https://neetcode.io/problems/is-palindrome
# Date: 2026-02-07
#


class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        filtered = ""

        for char in s.lower():
            if char.isalnum():
                filtered += char

        pointer_one = 0
        pointer_two = len(filtered) - 1

        while pointer_one < pointer_two:
            if filtered[pointer_one] != filtered[pointer_two]:
                return False

            pointer_one += 1
            pointer_two -= 1

        return True
