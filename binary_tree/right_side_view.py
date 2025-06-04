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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        Note:
            - return the right side view of the binary tree
                - imagining I'm standing on the right side of the tree looking to the tree
        Intuition:
            - BFS:
                - BFS traversal going from right most node first
                - store the first node at each node
        """

        # BFS:
        # TC: O(n) / SC: O(D) where D is diameter of the tree
        output = []
        if root is None:
            return output

        q = deque([root])
        while q:
            flag = False
            for _ in range(len(q)):
                node = q.popleft()

                if not flag:
                    output.append(node.val)
                    flag = True

                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)

        return output


solution = Solution()
start_time = time.time()
print(solution.rightSideView([1, 2, 3, None, 5, None, 4]))
print("--- %s seconds ---" % (time.time() - start_time))
