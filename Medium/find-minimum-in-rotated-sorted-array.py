#
# Problem: Find Minimum in Rotated Sorted Array
# Difficulty: Medium
# URL: https://neetcode.io/problems/find-minimum-in-rotated-sorted-array
# Date: 2026-03-06
#

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        min_value = float("inf")

        while left <= right:
            middle = left + ((right - left) // 2)
            
            if nums[left] <= nums[middle]:
                min_value = min(min_value, nums[left])
                left = middle + 1
            elif nums[middle] <= nums[right]:
                min_value = min(min_value, nums[middle])
                right = middle - 1

        return int(min_value)
