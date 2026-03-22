#
# Problem: Valid Binary Search Tree
# Difficulty: Medium
# URL: https://neetcode.io/problems/valid-binary-search-tree/question
# Date: 2026-03-22
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def checkSubtree(self, min_value: Optional[int], max_value: Optional[int], root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if min_value is not None and root.val <= min_value:
            return False
        if max_value is not None and root.val >= max_value:
            return False

        leftValid = self.checkSubtree(min_value, root.val, root.left) if root.left else True
        rightValid = self.checkSubtree(root.val, max_value, root.right) if root.right else True

        return leftValid and rightValid

        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        leftValid = self.checkSubtree(None, root.val, root.left) if root.left else True
        rightValid = self.checkSubtree(root.val, None, root.right) if root.right else True

        return leftValid and rightValid

        
