import time
from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set, Optional
from helper.functions import LinkedList, ListNode, Utility

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Leetcode 328
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # input:
            # head: ListNode || None
        # goal: group even and odd nodes together then merge the odd to even Linked List
        # Brainstorm:
            # Lead and Lag pointer approach:
                # lag starts at head
                # lead starts at the head.next
                # while lead is valid AND lead.next is valid:
                    # set lag.next to lead.next
                    # traverse lag to lag.next
                    # set lead.next to lag.next
                    # traverse lead to lead.next
        # Pseudocode:
            # set a basic if guard condition for empty head or invalid head.next:
                # if true, return head
            # set lag to head
            # set lead to head.next
            # set lead_head to lead (for quick reference when connecting odd to even)
            # while lead and lead.next is valid:
                # set lag.next to lead.next
                # traverse lag to lag.next
                # set lead.next to lag.next
                # traverse lead to lead.next
            # connect lag's tail with head of lead
            # return head
        if not head or not head.next:
            return head

        lag, lead = head, head.next
        lead_head = lead
        while lead and lead.next:
            lag.next = lead.next
            lag = lag.next

            lead.next = lag.next
            lead = lead.next

        lag.next = lead_head

        return head
    
solution = Solution()
input = LinkedList([3, 2, 1, 0])
Utility.print_linked_list(input.head)

start_time = time.time()
answer: ListNode = solution.reverseList(input.head)
print("--- %s seconds ---" % (time.time() - start_time))