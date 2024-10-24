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
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # with dummy node
        # slow starts from dummy rather than fast poitner starting from 1
        #     benefit:
        #         no need for fast.next.next check
        if not head:
            return None

        dummy = ListNode(0, head)
        mid, fast = dummy, head
        while fast and fast.next:
            fast = fast.next.next
            mid = mid.next
        
        mid.next = mid.next.next

        return dummy.next
    

class Solution1:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # input:
            # head: ListNode || None
        # goal: return the head of the node after removing the middle node of the Linked List
            # middle = n // 2
        # Brainstorm:
            # 1. Locate middle point
                # fast and slow pointer
                    # fast pointer will traverse the linked list twice as fast as slow pointer
                    # slow pointer will traverse the linked list at a normal pace
                # By the time fast reaches the end of the Linked list, slow will be half way done
                    # therefore, slow will be pointing to the middle node
                        # Gotcha:
                            # middle point is always pointing to the actual middle node:
                                # However, in order for us have access to the middle node's previous node, we'll have to reconfigure the mid point
                                    # Solution:
                                        # start the fast pointer one ahead of mid
                                            # in order for this to work, we need to traverse the fast and slow only while fast.next and fast.next.next are both valid
            # 2 - 3 Remove the middle point, Connect the middle's left node to the middle's right point
                # "mid" is pointing to actual middle node's previous node:
                    # set middle_node.next to middel_node.next.next
        # Pseudocode:
            # initialize fast and slow pointers
                # slow = head
                # fast = head.next
            # while fast.next and fast.next.next:
                # traverse the fast pointer to fast.next.next
                # traverse the slow pointer to slow.next
            # mid = slow
            # set mid.next = mid.next.next
            # return head
        # TC: O(n) / SC: O(1)
        # without dummy node:
        if not head or not head.next:
            return None

        mid, fast = head, head.next
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            mid = mid.next
        
        mid.next = mid.next.next

        return head


ll = LinkedList([1,3,4,7,1,2,6])
Utility.print_linked_list(ll.head)

solution = Solution1()
start_time = time.time()
answer = solution.deleteMiddle(ll.head)
print("--- %s seconds ---" % (time.time() - start_time))

Utility.print_linked_list(answer)