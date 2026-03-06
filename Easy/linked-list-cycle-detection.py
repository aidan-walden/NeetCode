#
# Problem: Linked List Cycle Detection
# Difficulty: Easy
# URL: https://neetcode.io/problems/linked-list-cycle-detection
# Date: 2026-03-06
#

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = {}

        node = head

        while node is not None:
            if node in visited:
                return True

            visited[node] = True
            node = node.next

        return False
