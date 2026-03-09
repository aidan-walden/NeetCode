#
# Problem: Merge K Sorted Linked Lists
# Difficulty: Hard
# URL: https://neetcode.io/problems/merge-k-sorted-linked-lists
# Date: 2026-03-08
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        result_head = None
        prev_node = None

        # next_elements stores the next element of each linked list
        # that must be appended to the answer.
        # next_elements[i] corresponds to the next element for the i-th list in `lists`
        next_elements = []

        smallest_node: Optional[ListNode] = None
        smallest_index = -1

        # populate element list with first node of each list
        # also find smallest_node for first iteration while we're here
        for i, head_node in enumerate(lists):
            next_elements.append(head_node)
            if smallest_node is None or (head_node is not None and head_node.val < smallest_node.val):
                smallest_node = head_node
                smallest_index = i

        
        def find_smallest():
            nonlocal smallest_node
            nonlocal smallest_index

            if smallest_node is not None:
                # here, we've already found smallest_node from the initial population loop
                # so, no need to loop again
                return

            for i, node in enumerate(next_elements):
                if node is None:
                    continue
                if smallest_node is None or node.val < smallest_node.val:
                    smallest_node = node
                    smallest_index = i

        while True:
            find_smallest()
            if smallest_node is None:
                return result_head

            if prev_node is None:
                result_head = ListNode(smallest_node.val)
                prev_node = result_head
            else:
                prev_node.next = ListNode(smallest_node.val)
                prev_node = prev_node.next


            next_elements[smallest_index] = smallest_node.next

            # reset smallest values for next iteration
            smallest_node = None
            smallest_index = -1
