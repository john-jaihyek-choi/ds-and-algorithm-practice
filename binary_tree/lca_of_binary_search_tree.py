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


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        """
        Note:
            - Binary Search Tree!!!
                - left smaller
                - right bigger
            - conditions:
                - if p == root:
                    - p is LCA
                - if q == root:
                    - q is LCA
                - elif p < root and q > root or p > root and q < root:
                    - root is LCA
                - elif p < root and q < root:
                    - traverse to the left
                - elif p > root and q > root:
                    - traverse to the left
        Intuition:
            - compare p and q value at each node
        """
        # TC: O(log n) / SC: O(1)
        node = root

        while node:
            if p.val < node.val and q.val < node.val:
                node = node.left
            elif p.val > node.val and q.val > node.val:
                node = node.right
            else:
                return node

        return node


solution = Solution()
start_time = time.time()
print(solution.lowestCommonAncestor([5, 3, 8, 1, 4, 7, 9, None, 2]))
print("--- %s seconds ---" % (time.time() - start_time))
