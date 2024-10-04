import pprint
import time
from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set, Optional
from helper.functions import LinkedList, ListNode, Utility

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