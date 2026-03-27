#
# Problem: Combination Sum
# Difficulty: Medium
# URL: https://neetcode.io/problems/combination-target-sum
# Date: 2026-03-27
#

class Solution:
    def _do_one(self, start_index: int, current_res: List[int], target: int):
        res = current_res[:]
        
        if target == 0:
            self.res.append(res)
            return
        if target < 0:
            return
        if start_index >= len(self.sorted_nums):
            return

        res.append(self.sorted_nums[start_index])

        # path 1: take this num and stay at i
        self._do_one(start_index, res, target - self.sorted_nums[start_index])

        res.pop()

        # path 2: skip this num, advance i
        self._do_one(start_index + 1, res, target)


    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.sorted_nums = sorted(nums)

        self.res = []

        self._do_one(0, self.res, target)
       
        return self.res


        
        
