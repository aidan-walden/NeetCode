#
# Problem: Longest Consecutive Sequence
# Difficulty: Medium
# URL: https://neetcode.io/problems/longest-consecutive-sequence
# Date: 2026-02-07
#

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0

        memo = {}

        def get_sequence_length(starting_num: int) -> int:
            if starting_num in memo:
                return 1 + get_sequence_length(starting_num + 1)
            elif starting_num in nums:
                memo[starting_num] = True
                return 1 + get_sequence_length(starting_num + 1)

            return 0

        for num in nums:
            seq_len = get_sequence_length(num)

            if seq_len > longest:
                longest = seq_len

        return longest
