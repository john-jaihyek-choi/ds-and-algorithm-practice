import time
import math
from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set, Optional
from helper.functions import LinkedList, ListNode, Utility

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # input:
            # head: ListNode || None
        # goal: group even and odd nodes together then merge the odd to even Linked List
        # Brainstorm:
            # Lead and Lag pointer approach:
                # lag starts at a dummy node
                # lead starts at the head
            # while lead is valid AND lead.next is valid:
                # set lag.next to lead.next
                # set lead.next to lag.next.next
                # traverse lead to lead.next
                # traverse lag to lag.next
        # Pseudocode:
            # create a dummy at ListNode(0, head)
            # initialize a lag and lead pointer
                # lag = dummy
                # lead = head
            # while lead and lead.next:
                # lag.next = lead.next
                # lead.next = lag.next.next
                # lead = lead.next
                # lag = lag.next
            # lead.next = lag
            # return dummy.next
        odd, even = ListNode(0, head), ListNode(0, head)
        lag, lead = even, head
        while lead and lead.next:
            lead_temp = lead.next
            lag_temp = lag.next

            lag.next = lead.next
            lead.next = lead.next.next
            
            lead = lead_temp
            lag = lag_temp
        

        lag.next = even.next
        return head

ll = LinkedList([1,2,3,4,5,6,7,8])
Utility.print_linked_list(ll.head)

solution = Solution()
start_time = time.time()
answer = solution.oddEvenList(ll.head)
print("--- %s seconds ---" % (time.time() - start_time))

Utility.print_linked_list(answer)