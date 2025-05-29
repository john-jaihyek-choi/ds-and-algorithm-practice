from collections import defaultdict, deque
from typing import List
from helper.functions import TreeNode
from typing import Optional
from binarytree import build
import time

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution2:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Note:
            - DFS
                - traverse to all left and right nodes
                - max depth is the sum of max left depth and max right depth
        """

        # DFS
        if root is None:
            return 0

        diameter = 0

        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0

            nonlocal diameter
            left = dfs(node.left)
            right = dfs(node.right)

            diameter = max(left + right, diameter)

            return max(left, right) + 1

        dfs(root)

        return diameter


class Solution1:
    # Pseudocode:
    # General idea:
    # recurse the tree, then compare the depth and the diameter at each recursion state
    # base case:
    # if root is None:
    # return 0
    # recurse:
    # recurse left
    # recurse right
    # compute the longer of the two:
    # max_diameter
    # height
    # return height
    # in the outer function, return max_diameter
    def __init__(self):
        self.max_diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dfs_height(root)

        return self.max_diameter

    def dfs_height(self, root: Optional[TreeNode]) -> int:
        # Base condition:
        if not root:
            return 0

        left = self.dfs_height(root.left)
        right = self.dfs_height(root.right)

        height = max(left, right)
        self.max_diameter = max(self.max_diameter, left + right)

        return height + 1


root = build([1, 2, 2, 3, None, None, 3, 4, None, None, 4])
print(root)
solution = Solution2()
start_time = time.time()
print(solution.diameterOfBinaryTree(root))
print("--- %s seconds ---" % (time.time() - start_time))
