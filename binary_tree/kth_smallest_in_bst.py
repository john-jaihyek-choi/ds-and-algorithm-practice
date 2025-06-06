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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Note:
            - smallest node of the bst is left bottom most node
                - the first node where its left node is a None
            - kth smallest node would be kth node from the smallest node when traversing the tree in "in-order"
        Intuition:
            - use an recursive DFS approach
                - do an inorder traversal on the tree, then store each node val in an array
                - return k-1th node's value
        """
        # DFS Recursive Optimized:
        smallest = root.val

        def dfs(node: TreeNode):
            nonlocal smallest, k
            if node is None:
                return

            dfs(node.left)
            k -= 1
            if k == 0:
                smallest = node.val
                return
            dfs(node.right)

        dfs(root)

        return smallest

        # DFS Recursive:
        # TC: O(n) / SC: O(n) for call stack and the output array
        tree = []

        def dfs(node: TreeNode):
            if node is None:
                return None

            dfs(node.left)
            tree.append(node.val)
            dfs(node.right)

        dfs(root)

        return tree[k - 1]


solution = Solution()
start_time = time.time()
print(solution.kthSmallest([5, 1, 4, None, None, 3, 6]))
print("--- %s seconds ---" % (time.time() - start_time))
