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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Note:
            - Valid BST:
                - left subtree of a node contains only nodes less than node itself
                - right subtree of a node contains only nodes greater than node itself
                - both left and right subtree must be BST
        Intuition:
            - DFS recursive:
                - traverse nodes DFS
                    - traverse to the left node
                    - traverse to the right node
                    - if node traversing is greater than the maximum
                        - return False
                    - if node traversing is less than the minimum
                        - return False
                    - else
                        - return True
        """

        # BFS:
        # TC: O(n) / SC: O(n)
        q = deque([(root, float("-inf"), float("inf"))])

        while q:
            for _ in range(len(q)):
                node, mn, mx = q.popleft()

                if not mn < node.val < mx:
                    return False

                if node.left:
                    q.append((node.left, mn, node.val))
                if node.right:
                    q.append((node.right, node.val, mx))

        return True

        # DFS Recursive:
        # TC: O(n) / SC: O(n)
        def dfs(node: TreeNode, minimum: int, maximum: int) -> Optional[int]:
            if node is None:
                return True

            if not (minimum < node.val < maximum):
                return False

            left, right = dfs(node.left, minimum, node.val), dfs(
                node.right, node.val, maximum
            )

            return left and right

        return dfs(root, float("-inf"), float("inf"))


solution = Solution()
start_time = time.time()
print(solution.isValidBST([5, 1, 4, None, None, 3, 6]))
print("--- %s seconds ---" % (time.time() - start_time))
