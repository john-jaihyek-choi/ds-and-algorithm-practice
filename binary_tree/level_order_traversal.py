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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Note:
            - Level order traversal
                - top to bottom, left to right
        Intuition:
            - use BFS:
                - traverse from the root node:
                    - use q to store each level of a tree
                    - append each node in the q's left and right nodes
        """
        # BFS
        # TC: O(n) / SC: O(n)
        output = []
        if root is None:
            return output

        q = deque([root])
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()

                level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            output.append(level)

        return output


solution = Solution()
start_time = time.time()
print(solution.levelOrder([3, 9, 20, None, None, 15, 7]))
print("--- %s seconds ---" % (time.time() - start_time))
