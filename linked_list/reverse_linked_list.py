import time
from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set, Optional
from helper.functions import LinkedList, ListNode, Utility

# Retried 10/24/2024: Leetcode 206
class Solution3:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # input:
            # head: ListNode or None
        # goal: reverse the linked list
        # Note:
            # iterative:
                # to reverse the order in place:
                    # the current head's next needs to point to None
                    # AND
                    # the current's next pointer should point to the cur
                # the above step must occur iteratively until the end of the node is reached

        # iterative method:
        # Pseudocode:
            # ex)
                # n c nxt
                #  [1, 2, 3, 4, 5]
            # initialize 2 different pointers
                # new pointing to None
                # cur pointing to head
            # while cur exists:
                # temp = cur.next
                # cur.next = new
                # new = cur
                # cur = temp
            # return new
        new, cur = None, head
        while cur:
            temp = cur.next
            cur.next = new
            new = cur
            cur = temp
        return new

        # Note:
            # recursive:
                # to reverse the order in place:
                    # we'll need to keep 2 pointers
                    # have a base case of head == None
                        # then return head
                    # in each iteration:
                        # recursively call reverseList and pass in head.next
        # recursive method:
            # ex)
                #   h  nh
                #  [1, 2, 3, 4, 5]
        # Pseudocode:
            # base case:
                # if head or head.next doesn't exit:
                    # return head
                # set new_head to the return value of the reverseList
                    # pass in head.next as the argument
                # set head.next.next = head
                # set head.next = None
                # return new_head
        if not head or not head.next:
            return head

        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return new_head

#  h        nh
# [1, 2, 3, 4]
# Solution 2: Recursive (TC: O(n) / SC: O(n))
class Solution2:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return new_head


# 1
# p  c t
# n [3,2,1,0]
# 2
#   p  c  t
# [ 3, 2, 1, 0 ]
# 3
#      p  c  t 
# [ 3, 2, 1, 0 ]

# Solution 1: Iterative (TC: O(n) / SC: O(1))
class Solution1:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new, cur = None, head

        while cur:
            temp = cur.next
            cur.next = new
            new = cur
            cur = temp
        
        return new
            


solution = Solution1()
input = LinkedList([3, 2, 1, 0])
Utility.print_linked_list(input.head)

start_time = time.time()
answer: ListNode = solution.reverseList(input.head)
print("--- %s seconds ---" % (time.time() - start_time))