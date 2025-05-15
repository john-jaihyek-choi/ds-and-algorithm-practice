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
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        Note:
            - given 2 non-empty linked list
            - l1 and l2 can be of different length
            - l1 and l2 are reversed
                ex) if l1 = [1,2,3], l2 = [4,5,6]
                    then l1 = 321 and l2 = 654
            - Things to consider:
                - carryover
                    - best a number could get is 18 + 1 = 19
                - l1 and l2 are already reversed, so the output is already reversed too
        Intuition:
            - traverse l1 and l2 together, sum up the value, then keep carryover
                - initialize carryover to 0
                - initialize new head for the sum value
                - initialize head1 and head2
                - traverse while head1 and head2
                    - set new.val to (head1.val + head2.val) % 10 + carryover
                    - carryover = (head1.val + head2.val) // 10
                    - set head1 to head1.next
                    - set head2 to head2.next
                - extend new.next to head1 or head2
                - if there's carryover:
                    - set new.next = Listnode(carryover)
        """

        carryover = 0
        head1, head2 = l1, l2
        dummy = new = ListNode()

        while head1 or head2 or carryover:
            h1 = head1.val if head1 else 0
            h2 = head2.val if head2 else 0
            sum_val = h1 + h2 + carryover
            remainder = sum_val % 10
            carryover = sum_val // 10
            new.next = ListNode(remainder)
            new = new.next
            head1, head2 = head1.next if head1 else None, head2.next if head2 else None

        return dummy.next


class Solution2:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        goal:
            given 2 non-empty linked lists with each node representing digit in each number, return sum of the 2 linked list
        edgecases:
            empty linked list
                - input is guaranteed to have non-empty lists
            different size of linked lists
                - no specification on constraints
                    - will assume if the size is different, I'll treat it as 0
        note:
            - Linked list already comes sorted
            - maximum value of sum of 2 numbers are 19
        intuition:
            - use carryover to track sum > 9
            - while l1 or l2 or carryover exists:
                - take sum of l1.val, l2.val, and carryover
                - update carryover with // 10
                - set remainder of sum to next val
        pseudocode:
            - intialize new ListNode with sum of l1 and l2 head (new)
            - traverse while l1 or l2 or carryover:
                - sum_val = l1.val + l2.val + carryover
                - carryover = sum_val // 10
                    - 1 if >= 10
                    - 0 else
                - set sum_val % 10 to next
        """

        new = cur = ListNode()
        carryover = 0
        while l1 or l2 or carryover:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            sum_val = (l1_val + l2_val) + carryover

            carryover = sum_val // 10
            cur.next = ListNode(sum_val % 10)

            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return new.next


class Solution1:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
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
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
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


solution = Solution2()
l1 = [2, 4, 3]
l2 = [5, 6, 4]
start_time = time.time()
answer = solution.addTwoNumbers(l1, l2)
print("--- %s seconds ---" % (time.time() - start_time))

Utility.print_linked_list(answer)
