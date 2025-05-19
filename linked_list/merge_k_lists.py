import time
from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set, Optional
from helper.functions import LinkedList, ListNode, Utility


# Leetcode 23
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Note:
            - k linked lists in input lists
                - k is not fixed
            - return merged linked list in single list
            - values are in ascending order
        Intuition:
            - Bruteforce:
                - General idea:
                    - initialize an empty LinkedList head
                    - iterate on lists to merge 1 array at a time
                - initialize dummy head for output list
                - iterate on lists:
                    - for each list, merge two linked list
        """

        # 1. Bruteforce:
        # TC: O(n * k) / SC: O(1)
        dummy = new = ListNode(float("-inf"))  # SC: O(1)

        for lst in lists:  # TC: O(k) / SC: O(1)
            new = self.mergeTwoLists(new, lst)  # TC: O(n)

        return dummy.next

    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> ListNode:
        head1, head2 = list1, list2
        dummy = new = ListNode(float("-inf"))

        while head1 and head2:
            if head1.val <= head2.val:
                new.next = head1
                head1 = head1.next
            else:
                new.next = head2
                head2 = head2.next
            new = new.next

        new.next = head1 or head2

        return dummy.next


solution = Solution()
input = LinkedList([3, 2, 1, 0])
Utility.print_linked_list(input.head)

start_time = time.time()
answer: ListNode = solution.mergeKLists(input.head)
print("--- %s seconds ---" % (time.time() - start_time))
