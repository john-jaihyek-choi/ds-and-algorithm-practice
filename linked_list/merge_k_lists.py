import time
from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set, Optional
from helper.functions import LinkedList, ListNode, Utility


# Leetcode 23
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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
            - Time optimization:
                - Instead of merging lists one by one, I merge lists by 2
                - General steps:
                    - initialize an empty list to start at
                    - while len(list) > 1:
                        - iterate lists at an increment of 2
                            - merge lists[i] and lists[i + 1]
                            - append merged list to a temporary merged llist
                            - set list to merged list
        """

        # 2. Optimal time:
        # TC: O(n * log k) / SC: O(k)
        if not lists:
            return None

        while len(lists) > 1:
            merged = []  # SC: O(k)
            for i in range(0, len(lists), 2):  # TC: O(log k)
                l1, l2 = lists[i], lists[i + 1] if i + 1 < len(lists) else None
                merged.append(self.mergeTwoLists(l1, l2))  # TC: O(n1 + n2) -> O(n)

            lists = merged

        return lists[0]

        # 1. Bruteforce:
        dummy = new = ListNode(float("-inf"))  # SC: O(n)

        for i, lst in enumerate(lists):  # TC: O(k) / SC: O(n)
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
