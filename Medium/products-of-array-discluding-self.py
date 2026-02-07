#
# Problem: Products Of Array Discluding Self
# Difficulty: Medium
# URL: https://neetcode.io/problems/products-of-array-discluding-self
# Date: 2026-02-07
#

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []

        memo_left = {}
        memo_right = {}

        for i, num in enumerate(nums):

            def find_product_left(index):
                if index < 0:
                    return 1
                if index in memo_left:
                    return memo_left[index]
                elif index == 1:
                    return nums[0] * nums[1]
                elif index == 0:
                    return nums[0]
                
                result = nums[index] * find_product_left(index - 1)
                memo_left[index] = result
                return result

            def find_product_right(index):
                if index > len(nums) - 1:
                    return 1
                if index in memo_right:
                    return memo_right[index]
                elif index == len(nums) - 2:
                    return nums[-1] * nums[-2]
                elif index == len(nums) - 1:
                    return nums[-1]

                result = nums[index] * find_product_right(index + 1)
                memo_right[index] = result
                return result

            this_product = find_product_left(i - 1) * find_product_right(i + 1)
            output.append(this_product)

        return output
