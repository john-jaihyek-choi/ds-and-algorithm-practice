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
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 2. Find the mid point of the list, reverse the second half, then merge
            # Find mid point:
                # initialize a fast and slow pointer, both starting at the same position
                    # fast, slow = head, head
                # while fast and fast.next is valid:
                    # fast = fast.next.next
                    # slow = slow.next
            # reverse the right half of the list
                # initialize new and cur nodes
                    # new = None
                    # cur = slow.next
                # while cur is valid
                    # temp = cur.next
                    # cur.next = new
                    # new = cur
                    # cur = temp
                # return new
            # store the reversed right list
                # right head starts at new
            # store left list
                # left head starts at head
            # (IMPORTANT) disconnect the end of the left from start of the right list
                # since slow is the end of the left list, set slow.next to None
                    # This operation can be done here since we are storing right list already
            # merge the left and right list
                # while left and right are valid
                    # store the l_temp variable for left.next
                    # store the r_temp variable for right.next
                    # set left.next to right
                    # set right.next to l_temp
                    # set left to l_temp
                    # set right to r_temp
            # return the function with no value

        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        new, cur = None, slow.next
        while cur:
            temp = cur.next
            cur.next = new
            new = cur
            cur = temp

        slow.next = None
        left, right = head, new

        while left and right:
            l_temp, r_temp = left.next, right.next

            left.next = right
            right.next = l_temp

            left, right = l_temp, r_temp
        
        return

class Solution1:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Brainstorm:
            # the pattern is pretty much alternating between first in the list and last in the list
            # if I have access to the tail, I'd be able to start from each end.
                # However, because the input is a singly linked list, I won't have access to tail nor the prev nodes
            # if space is not a concern,
                # I can iterate the nodes and store the value of the nodes in an array,
                    # then from the array, create a new node in a particular order.

        # 1. iterating and storing the nodes in array:
            # if head is None:
                # return
            # initialize an empty array to store the nodes (node_list)
            # initialize node at head
            # iterate on the node until node is None
                # in each iteration;
                    # store each node in the array
                    # set node to node.next
            # initialize a 2 pointers, l and r
                # l starting from 0
                # r starting from len(node_list) - 1
            # while l < r:
                # store a temp variable for left node's next node (temp)
                # set left node's next to right node
                # set right node's next to temporary node stored
                # increment l by 1
                # decrement r by 1
            # (IMPORTANT) disconnect the end of left list's next to None
                # this is required to disconnect the cycle connecting left list's next from pointing to the original next value
            # return

        if not head:
            return

        node_list = []

        node = head
        while node:
            node_list.append(node)
            node = node.next

        l, r = 0, len(node_list) - 1
        while l < r:
            temp = node_list[l].next

            node_list[l].next = node_list[r]
            node_list[r].next = temp
            
            l += 1
            r -= 1
        
        node_list[l].next = None
        
        return 


input1 = LinkedList([2,4,6,8])
Utility.print_linked_list(input1.head)

solution = Solution1()
start_time = time.time()
answer = solution.reorderList(input1.head)
print("--- %s seconds ---" % (time.time() - start_time))

Utility.print_linked_list(answer)