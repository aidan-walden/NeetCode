#
# Problem: 3Sum
# Difficulty: Medium
# URL: https://neetcode.io/problems/three-integer-sum
# Date: 2026-02-18
#

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
            nums_sorted = sorted(nums)

            output = []

            end = len(nums) - 1

            for i, num in enumerate(nums_sorted):
                if num > 0:
                    break

                if i > 0 and num == nums_sorted[i - 1]:
                    continue
                pointer_one = i + 1
                pointer_two = end

                while pointer_one < pointer_two:
                    num_one = nums_sorted[pointer_one]
                    num_two = nums_sorted[pointer_two]

                    s = num_one + num_two + num

                    if s == 0:
                        output.append([num, num_one, num_two])
                        pointer_one += 1
                        pointer_two -= 1

                        # skip duplicates on left
                        while pointer_one < pointer_two and nums_sorted[pointer_one] == nums_sorted[pointer_one - 1]:
                            pointer_one += 1
                        # skip duplicates on right
                        while pointer_one < pointer_two and nums_sorted[pointer_two] == nums_sorted[pointer_two + 1]:
                            pointer_two -= 1
                    elif s < 0:
                        pointer_one += 1
                    else:
                        pointer_two -= 1

            return output
