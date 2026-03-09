#
# Problem: Invert Binary Tree
# Difficulty: Easy
# URL: https://neetcode.io/problems/invert-a-binary-tree
# Date: 2026-03-08
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        self.invertTree(root.left)
        self.invertTree(root.right)

        orig_left = root.left
        orig_right = root.right

        root.left = orig_right
        root.right = orig_left

        return root
