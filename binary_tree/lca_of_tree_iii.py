from collections import defaultdict, deque
from typing import List
from helper.functions import TreeNode
from typing import Optional
from binarytree import build
import time


"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""


class Solution:
    def lowestCommonAncestor(self, p: "Node", q: "Node") -> "Node":
        """
        Space optimization using depth pointer with iteration rather than recursion
        """

        # TC: O(n) / SC: O(1)
        p_depth = self.getDepth(p)
        q_depth = self.getDepth(q)

        shallow_node = p if p_depth <= q_depth else q
        deeper_node = p if p_depth > q_depth else q

        # move deeper node up
        if p_depth != q_depth:
            deeper_node = self.traverseUp(deeper_node, abs(p_depth - q_depth))

        while shallow_node != deeper_node:
            shallow_node = self.traverseUp(shallow_node, 1)
            deeper_node = self.traverseUp(deeper_node, 1)

        return shallow_node

    def traverseUp(self, node, step):
        for _ in range(step):
            node = node.parent

        return node

    def getDepth(self, node: "Node") -> int:
        depth = 0

        while node:
            node = node.parent
            depth += 1

        return depth


class Solution2:
    def lowestCommonAncestor(self, p: "Node", q: "Node") -> "Node":
        """
        Slight Space optimization using depth pointer
            - but still with recursion stack
        """

        # TC: O(n) / SC: O(n)
        p_depth = self.getDepth(p, 0)
        q_depth = self.getDepth(q, 0)

        shallow_node = p if p_depth <= q_depth else q
        deeper_node = self.traverseUp(
            p if p_depth > q_depth else q, abs(p_depth - q_depth)
        )

        while shallow_node and deeper_node and shallow_node.val != deeper_node.val:
            shallow_node = shallow_node.parent
            deeper_node = deeper_node.parent

        return shallow_node

    def traverseUp(self, node, step):
        if step == 0:
            return node

        return self.traverseUp(node.parent, step - 1)

    def getDepth(self, node: "Node", depth: int) -> int:
        if node is None:
            return depth

        return self.getDepth(node.parent, depth + 1)


class Solution1:
    def lowestCommonAncestor(self, p: "Node", q: "Node") -> "Node":
        """
        Note:
            - LCA:
                - lowest node that has both p and q as decendants
                - the p or q node can be LCA of itself
        Intuition:
            - 2 Pass to store path to p and q, then iterate the stored paths as long as they are match
                - DFS traversal for p to root
                - DFS traversal for q to root
                    - if the node traversing is p, return the p.val
                - iterate from the end of each array and find the first matching number
        """

        # TC: O(n) / SC: O(n)
        def dfs(node: "Node", lst: List["Node"]) -> List["Node"]:  # TC: O(n) / SC: O(n)
            if node is None:
                return lst

            lst.append(node)
            dfs(node.parent, lst)
            return lst

        p_path = dfs(p, [])  # SC: O(n)
        q_path = dfs(q, [])  # SC: O(n)

        p1, p2 = len(p_path) - 1, len(q_path) - 1
        while (p_path[p1] and q_path) and p_path[p1].val == q_path[p2].val:  # TC: O(k)
            p1 -= 1
            p2 -= 1

        return p_path[p1 + 1]


solution = Solution2()
start_time = time.time()
print(solution.verticalOrder([3, 9, 20, None, None, 15, 7]))
print("--- %s seconds ---" % (time.time() - start_time))
