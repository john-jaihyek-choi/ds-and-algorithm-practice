from collections import defaultdict
from typing import List
from helper.functions import TreeNode
from typing import Optional
import time
from binarytree import build

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Note:
            - for each node, switch left with right
                - dfs to left
                - dfs to right
            - dfs function:
                - base case: node is None
        """
        # BFS
        if root is None:
            return None

        stack = [root]

        while stack:
            node = stack.pop()

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

            node.left, node.right = node.right, node.left

        return root

        # DFS
        if root is None:
            return None

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


root = build([1, 2, 3, 4, 5, 6, 7])
print(root)
solution = Solution()
start_time = time.time()
print(solution.invertTree(root))
print("--- %s seconds ---" % (time.time() - start_time))
