#
# Problem: Container With Most Water
# Difficulty: Medium
# URL: https://neetcode.io/problems/max-water-container
# Date: 2026-02-23
#

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        bestArea = -1

        p_left = 0
        p_right = len(heights) - 1

        while p_right > p_left:
            h_left = heights[p_left]
            h_right = heights[p_right]

            container_height = min(h_left, h_right)
            container_width = p_right - p_left

            container_area = container_height * container_width

            if container_area > bestArea:
                bestArea = container_area

            if h_left > h_right:
                p_right -= 1
            elif h_left < h_right:
                p_left += 1
            else:
                p_right -= 1
                p_left += 1

        return bestArea
