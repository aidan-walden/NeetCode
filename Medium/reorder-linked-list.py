#
# Problem: Reorder Linked List
# Difficulty: Medium
# URL: https://neetcode.io/problems/reorder-linked-list
# Date: 2026-03-08
#

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None:
            return

        node_left = head

        node_right = node_left.next

        if node_right is None:
            return

        while node_right.next is not None:
            node_right = node_right.next

        while node_left != node_right:
            if node_left is None:
                break

            old_nr = node_right

            # n-1 -> 1
            node_right.next = node_left.next

            # 0 -> n-1
            node_left.next = node_right

            node_left = node_right.next

            node_right = node_left

            while node_right.next != old_nr:
                if node_right.next is None:
                    break
                node_right = node_right.next

        node_right.next = None
