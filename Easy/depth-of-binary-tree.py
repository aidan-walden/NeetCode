#
# Problem: Maximum Depth of Binary Tree
# Difficulty: Easy
# URL: https://neetcode.io/problems/depth-of-binary-tree
# Date: 2026-03-08
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
