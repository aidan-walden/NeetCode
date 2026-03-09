#
# Problem: Remove Node From End of Linked List
# Difficulty: Medium
# URL: https://neetcode.io/problems/remove-node-from-end-of-linked-list
# Date: 2026-03-08
#

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ll_len = 1

        this_node = head

        while this_node and this_node.next is not None:
            this_node = this_node.next
            ll_len += 1

        prev_node = None
        this_node = head
        i = 0

        while i < ll_len - n:
            prev_node = this_node
            this_node = this_node.next if this_node else None
            i += 1

        if prev_node is None:
            # remove 1st element
            return head.next if head else None

        if this_node is None:
            return None

        prev_node.next = this_node.next

        return head
