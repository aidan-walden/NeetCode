#
# Problem: Reverse Linked List
# Difficulty: Easy
# URL: https://neetcode.io/problems/reverse-a-linked-list
# Date: 2026-03-06
#

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []

        this_node = head

        while this_node is not None:
            nodes.append(this_node.val)
            this_node = this_node.next

        if len(nodes) == 0:
            return head

        new_node = ListNode(nodes.pop())
        eval_node = new_node
        
        while len(nodes) > 0:
            next_node = ListNode(nodes.pop())
            eval_node.next = next_node
            eval_node = eval_node.next


        return new_node
