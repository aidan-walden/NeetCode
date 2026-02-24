#
# Problem: Trapping Rain Water
# Difficulty: Hard
# URL: https://neetcode.io/problems/trapping-rain-water
# Date: 2026-02-24
#

class Solution:
    def trap(self, height: List[int]) -> int:
        trapped_water = 0

        max_left, max_right = 0, 0

        p_left = 0
        p_right = len(height) - 1

        while p_left < p_right:
            if height[p_left] > max_left:
                max_left = height[p_left]

            if height[p_right] > max_right:
                max_right = height[p_right]

            if max_left <= max_right:
                p_left += 1
                trapped_water += max(0, max_left - height[p_left])
            else:
                p_right -= 1
                trapped_water += max(0, max_right - height[p_right])

        return trapped_water
