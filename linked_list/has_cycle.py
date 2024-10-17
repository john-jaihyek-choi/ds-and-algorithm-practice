import time
import math
from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set, Optional
from helper.functions import LinkedList, ListNode, Utility


class Solution2:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # fast and slow pointer approach:
            # initialize fast and slow to head
            # iteratate while fast and fast.next is valid:
                # traverse fast twice as fast as slow
                # traverse slow at normal pace
                # if fast == slow
                    # return True
            # return False

        # TC: O(n) / SC: O(1)
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True

        return False

class Solution1:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # less efficient hash approach:
            # initialize an empty dictionary to hash the nodes
            # set a cur to iterate on, starting from head
            # while cur is valid:
                # if cur.next is in dictionary:
                    # return True
                # store the cur node to the dictionary
                # traverse the cur to cur.next
            # return false

        # TC: O(n) / SC: O(n)
        node_map = {}
        cur = head
        while cur:
            if cur.next in node_map:
                return True
            node_map[cur] = None
            cur = cur.next
        
        return False


input1 = LinkedList([1,2,3,4])
Utility.print_linked_list(input1.head)

solution = Solution2()
start_time = time.time()
answer = solution.hasCycle(input1.head)
print("--- %s seconds ---" % (time.time() - start_time))

print(answer)