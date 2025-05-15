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


class Solution2:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Note:
            - remove nth node from the linked list
                - ex) if n = 2 where list = [1,2,3,4]
                    - 3 should be removed
        Intuition:
            - use lead pointer, then iterate til lead is None
                - initialize lead pointer at head, lag pointer at dummy that points to head
                - iterate n many times and traverse lead pointer
                - iterate lead and lag pointer while lead is valid
                - disconnect lag.next and connect with lag.next.next
        """

        dummy = ListNode(0, head)
        lag, lead = dummy, head
        for i in range(n - 1):
            lead = lead.next

        while lead and lead.next:
            lag = lag.next
            lead = lead.next

        lag.next = lag.next.next

        return dummy.next


class Solution1:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Using lead lag pointer:
        # set the lead pointer to head
        # iterate the head initially to traverse to node at n (range starting from 1 to n ** 1 as starting for 1-indexing)
        #      0  1  2  3
        # ex) [1, 2, 3, 4] , n = 2
        #      ^     ^
        #     lag  lead
        # lead  = n + 1
        # set the lag pointer to head
        # iterate while lead pointer is valid
        # set lag.next = lag.next.next
        # return the head

        # TC: O(n) / SC: O(1)
        lead = head
        for _ in range(1, n):
            lead = lead.next

        new_node = lag = ListNode(None, head)
        while lead and lead.next:
            lag = lag.next
            lead = lead.next

        lag.next = lag.next.next

        return new_node.next

    def removeNthFromHead(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # create a dummy node and assign next to the head
        # make a cur pointer point to the dummy node
        # iterate n many times starting from 1 (equivalent to n - 1)
        # set cur to cur.next to traverse
        # set cur.next to cur.next.next
        # return next node of the dummy node

        # TC: O(n) / SC: O(1)
        new_node = cur = ListNode(None, head)
        for _ in range(1, n):  # stop at the (n-1)th node
            cur = cur.next

        cur.next = cur.next.next

        return new_node.next


ll = LinkedList([1])
Utility.print_linked_list(ll.head)

solution = Solution1()
start_time = time.time()
answer = solution.removeNthFromHead(ll.head, 1)
print("--- %s seconds ---" % (time.time() - start_time))

Utility.print_linked_list(answer)
