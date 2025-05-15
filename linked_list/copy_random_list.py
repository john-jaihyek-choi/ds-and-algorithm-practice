import time
import math
from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set, Optional
from helper.functions import LinkedList, ListNode, Utility


class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution2:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        """
        Note:
            - Create a deep copy of the linked list provided as input
                - Copied_Node.random must also point to new node in the deep copy
            - Are the values unique?
                - No
            - Return the copied Linked List
        Intuition:
            - Use dictionary to create reference between original and new node copies:
                - ex)
                    {
                        None: None,
                        Node(7): New_Node(7),
                        Node(13): New_Node(13),
                        ...
                    }
            - iterate on original head and add every existing node to the dictionary
            - iterate again from the head, set next and random pointer of Node(val) to a key in the dictionary
        """

        # TC: O() / SC: O()
        ref = {None: None}  # SC: O(n)

        cur = head
        while cur:  # SC: O(n)
            ref[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur:  # SC: O(n)
            ref[cur].next = ref[cur.next]
            ref[cur].random = ref[cur.random]
            cur = cur.next

        return ref[head]


# First try
class Solution1:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        """
        # Each copied node to dictionary, then reassign next and random approach:
            # initialize an initial dictionary with {None: None} dictionary to store the copied_nodes (node_dict)
            # cur = head
            # iterate on cur while valid:
                # create a new node with val as cur.val (copied_node)
                # store the copied_node as a value in a dictionary (node_dict) with key as cur
            # new_head = lag = ListNode(None, head)
            # lead = lag.next
            # iterate while lead is valid:
                # new_node = node_dict[lead]
                # new_node.next = node_dict[lead.next]
                # new_node.random = node_dict[lead.random]
                # temp = lag.next
                # lag.next = new_node
                # lead = lead.next
                # lag = temp
            # return new_head.next
        """
        # TC: O(n) / SC: O(n)
        node_dict = dict({None: None})
        cur = head
        while cur:  # O(n)
            node_dict[cur] = Node(cur.val)  # O(1)
            cur = cur.next  # O(1)

        new_head = lag = Node(0, head)  # O(1)
        lead = head  # O(1)
        while lead:  # O(n)
            new_node = node_dict[lead]  # O(1)
            new_node.next = node_dict[lead.next]  # O(1)
            new_node.random = node_dict[lead.random]  # O(1)

            temp = lag  # O(1)
            lag.next = new_node  # O(1)
            lead = lead.next  # O(1)
            lag = temp.next  # O(1)

        return new_head.next  # O(1)


solution = Solution1()
start_time = time.time()
answer = solution.copyRandomList([[3, None], [7, 3], [4, 0], [5, 1]])
print("--- %s seconds ---" % (time.time() - start_time))

Utility.print_linked_list(answer)
