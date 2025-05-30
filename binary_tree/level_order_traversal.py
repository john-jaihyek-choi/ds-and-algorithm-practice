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
            - Level order traversal:
                - layer (horizontal) by layer
        Intuition:
            - BFS:
                - queue to store each layer
                - traverse starting from root node
                    - iterate len(q)
                        - store node val to the q
                        - append node val to output array
        """

        # TC: O(n) / SC: O(n)
        output = []
        if root is None:
            return output

        q = deque([root])

        while q:
            layer = []
            for _ in range(len(q)):
                node = q.popleft()
                layer.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            output.append(layer)

        return output


solution = Solution()
start_time = time.time()
print(solution.levelOrder([3, 9, 20, None, None, 15, 7]))
print("--- %s seconds ---" % (time.time() - start_time))
