import time
import math
from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set, Optional
from helper.functions import LinkedList, ListNode, Utility

# Solution 2: Recursive method
class Solution1:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Pseudocode:
            # 


    
# Solution 1: Iterative method
class Solution1:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Note:
            # list1 and list2 are sorted
            # must return the head of the merged list
            # Special Conditions:
                # if one of the two, list1 and list2, is empty, return the head of the non-empty list
                # if list1 and list2 are both empty, return the dummy node
                # to handle the above 2 cases properly, I'll need a dummy node at the beginning

        # Pseudocode:
            # initialize a dummy node and a pointer to the initial dummy node
            # while list1 and list2 are non empty:
                # if list1.val <= list2.val:
                    # set node.next to list1 node
                    # set list1 to list1.next (this allows traversal to next node in list1)
                # else: (list2.val is smaller than list1.val)
                    # set node.next to list2 node
                    # set list2 to list2.next (this allows traversal to next node in list2)
                # set the current node pointer to node.next (this allows traversal to next node since we've set node.next value above)
            # set node.next to non-empty lists, either list1 or list2
                # this is because we need to get the non-empty list and append it to the end of our current node
            # return dummy.next (dummy here contains the head of the dummy node created at the beginning of the function)

        new_node = node = ListNode()
        
        while list1 and list2: # O(n)
            if list1.val <= list2.val: # O(1)
                node.next = list1 # O(1)
                list1 = list1.next # O(1)
            else: # O(1)
                node.next = list2 # O(1)
                list2 = list2.next # O(1)
            node = node.next # O(1)
        
        node.next = list1 or list2 # O(1)

        return new_node.next



input1 = LinkedList([1, 2, 4])
input2 = LinkedList([1, 3, 5])
Utility.print_linked_list(input1.head)
Utility.print_linked_list(input2.head)

solution = Solution1()
start_time = time.time()
answer = solution.mergeTwoLists(input1.head, input2.head)
print("--- %s seconds ---" % (time.time() - start_time))

Utility.print_linked_list(answer)