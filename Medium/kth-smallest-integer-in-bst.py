#
# Problem: Kth Smallest Integer in BST
# Difficulty: Medium
# URL: https://neetcode.io/problems/kth-smallest-integer-in-bst
# Date: 2026-03-22
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findSmallest(self, root: Optional[TreeNode], k: int) -> tuple[int, int]:
        if not root:
            return 0, -1
        count, found_value = self.findSmallest(root.left, k)
        if count == k:
            # the node we just got back had the nth smallest value
            return count, found_value

        count += 1 # the left node wasn't it, so let's try the node we're visiting right now
        if count == k:
            return count, root.val
        else:
            # finally, try the right node
            # subtract count from k to account for the nodes we've already visited
            right_count, found_value = self.findSmallest(root.right, k - count)
            count += right_count
            if count == k:
                return count, found_value
        return count, -1
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1
        _, found_value = self.findSmallest(root, k)
        return found_value
