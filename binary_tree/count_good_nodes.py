from collections import defaultdict, deque
from typing import List
from helper.functions import TreeNode
from typing import Optional
from binarytree import build
import time

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# input:
# root: TreeNode
# root of the input binary tree
# outpug:
# output: int:
# the count of good nodes in the given binary tree
# Note:
# Node is a good node if value to the left


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        Note:
            - Good Node:
                - node where none of the node's parent's path are greater than itself
        Intuition:
            - DFS Recursive:
                - DFS traversal from the root
                    - at each traversal check with the max value (max starts at inf)
                    - if node traversing's value is less than the path's min, don't increment counter
                    - else, increment good counter
        """

        # BFS:
        # TC: O(n) / SC: O(n)
        if root is None:
            return 0

        q = deque([(root, root.val)])
        good = 0

        while q:
            for _ in range(len(q)):
                node, maximum = q.popleft()

                if node.val >= maximum:
                    good += 1
                if node.left:
                    q.append((node.left, max(maximum, node.val)))
                if node.right:
                    q.append((node.right, max(maximum, node.val)))

        return good

        # DFS Iterative:
        # TC: O(n) / SC: O(n)
        if root is None:
            return 0

        stack = [(root, root.val)]
        good = 0
        while stack:
            node, maximum = stack.pop()

            if node.val >= maximum:
                good += 1

            if node.left:
                stack.append((node.left, max(maximum, node.val)))
            if node.right:
                stack.append((node.right, max(maximum, node.val)))

        return good

        # DFS Recursive:
        # TC: O(n) / SC: O(n)
        if root is None:
            return 0

        good = 0

        def dfs(node: TreeNode, maximum: int) -> None:
            nonlocal good

            if node is None:
                return

            if node.val >= maximum:
                good += 1

            dfs(node.left, max(maximum, node.val))
            dfs(node.right, max(maximum, node.val))

        dfs(root, root.val)

        return good


"""
good at 2
good at 4
good at 10
good at 8
good at 4
"""


solution = Solution()
start_time = time.time()
print(solution.rightSideView([1, 2, 3, None, 5, None, 4]))
print("--- %s seconds ---" % (time.time() - start_time))
