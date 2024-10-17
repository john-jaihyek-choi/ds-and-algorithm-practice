import time
import math
from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set, Optional
from helper.functions import LinkedList, Utility

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # This solution is invalid due to creation of empty ListNode
            # The creation of empty ListNode is required to prevent from None type error on cur.val
            # But when I set empty ListNode with value 0, it would be creating leading zero (0 at the last node) on certain cases

        # iterate the l1 and l2, compute the numbers in order of 1th, 10th, 100th...
            # create a dummy node to add the nodes to (new_node)
            # set cur to dummy node (cur = new_node)
            # initialize carry_over to 0
            # while l1 or l2 is non-empty or carry_over is valid:
                # store l1.val and l2.val
                    # Value to 0 if none
                # compute sum of l1.val, l2.val, and carry_over
                # set carry_over to sum // 10
                    # 0 if sum is below 10
                    # 1 if sum is greater than or equal to 10
                # set cur.next to ListNode(sum % 10)
                    # set the remainder of sum / 10 as a value for the next node
                # if l1 is non-empty:
                    # traverse l1 node to next
                # if l2 is non-empty:
                    # traverse l2 node to next
                # traverse cur to cur.next
            # return new_node.next

        new_node = cur = ListNode()
        carry_over = 0
        while l1 or l2 or carry_over:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            
            sum = l1_val + l2_val + carry_over
            
            carry_over = sum // 10
            cur.next = ListNode(sum % 10)
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            cur = cur.next

        return new_node.next


class InvalidSolution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # This solution is ***INVALID*** due to creation of empty ListNode
            # The creation of empty ListNode is required to prevent from None type error on cur.val
            # But when I set empty ListNode with value 0, it would be creating leading zero (0 at the last node) on certain cases

        # iterate the l1 and l2, compute the numbers in order of 1th, 10th, 100th...
            # create a dummy node to add the nodes to (new_node)
            # set cur to dummy node (cur = new_node)
            # while l1 or l2 is non-empty:
                # if l1 is non-empty and l2 is non-empty:
                    # sum = l1.val + l2.val
                # else:
                    # num = l1 or l2
                    # sum = num.val
                # if sum >= 10
                    # set cur.next equal to new ListNode with val 1
                # set cur.val equal to sum of itself and the sum
                # if l1 is non-empty:
                    # traverse l1 node to next
                # if l2 is non-empty:
                    # traverse l2 node to next
                # traverse cur to cur.next
            # return new_node

        new_node = cur = ListNode()

        while l1 or l2:
            if l1 and l2:
                sum = l1.val + l2.val
            else:
                valid_node = l1 or l2
                sum = valid_node.val
            
            if sum >= 10:
                cur.next = ListNode(1)
            else:
                cur.next = ListNode()

            cur.val += sum % 10
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            cur = cur.next

        return new_node




solution = Solution()
start_time = time.time()
answer = solution.copyRandomList([[3, None],[7,3],[4,0],[5,1]])
print("--- %s seconds ---" % (time.time() - start_time))

Utility.print_linked_list(answer)