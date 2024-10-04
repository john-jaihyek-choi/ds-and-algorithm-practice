import pprint
from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set, Optional
import time
import math

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def to_list(head: ListNode):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


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
            

node4 = ListNode(4, None)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)
solution = Solution2()
start_time = time.time()
answer = solution.reverseList(node1)
pprint.pprint(to_list(answer))
print("--- %s seconds ---" % (time.time() - start_time))