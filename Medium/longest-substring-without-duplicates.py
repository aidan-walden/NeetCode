#
# Problem: Longest Substring Without Repeating Characters
# Difficulty: Medium
# URL: https://neetcode.io/problems/longest-substring-without-duplicates
# Date: 2026-03-02
#

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_characters = {}
        best_length = 0
        left = 0

        for right, char in enumerate(s):
            if char in seen_characters and seen_characters[char] >= left:
                left = seen_characters[char] + 1

            seen_characters[char] = right

            best_length = max(best_length, right - left + 1)

        return best_length
