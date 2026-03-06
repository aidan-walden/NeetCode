#
# Problem: Merge Two Sorted Linked Lists
# Difficulty: Medium
# URL: https://neetcode.io/problems/merge-two-sorted-linked-lists
# Date: 2026-03-06
#

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        
        sorted_list = []
        array1 = []
        array2 = []

        list1_head = list1

        while list1_head is not None:
            array1.append(list1_head.val)
            list1_head = list1_head.next

        list2_head = list2

        while list2_head is not None:
            array2.append(list2_head.val)
            list2_head = list2_head.next

        pointer_one = 0
        pointer_two = 0

        while pointer_one < len(array1) or pointer_two < len(array2):
            val_one = array1[pointer_one] if pointer_one < len(array1) else float("inf")
            val_two = array2[pointer_two] if pointer_two < len(array2) else float("inf")

            if val_one < val_two:
                sorted_list.append(val_one)
                pointer_one += 1
            elif val_one > val_two:
                sorted_list.append(val_two)
                pointer_two += 1
            else:
                sorted_list.append(val_one)
                sorted_list.append(val_two)
                pointer_one += 1
                pointer_two += 1

        new_node = ListNode(sorted_list[0])
        eval_node = new_node

        pointer = 1
        while pointer < len(sorted_list):
            next_node = ListNode(sorted_list[pointer])
            eval_node.next = next_node
            eval_node = eval_node.next
            pointer += 1

        return new_node
