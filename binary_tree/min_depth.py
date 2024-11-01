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

# iterative BFS approach - TC: O(n) / SC: O(w) w = nodes in the breadth:
class Solution1:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0

        q = deque([root])
        min_depth = 0

        while q:

            for _ in range(len(q)):
                node = q.popleft()

                if not node.left and not node.right:
                    return min_depth + 1

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            min_depth += 1
        
        return min_depth

# recursive DFS approach (Less efficient) - TC: O(n) / SC: O(h)
class Solution2:
    def minDepth(self, root: Optional[TreeNode]) -> int:
    # DFS approach - TC: O(n) / SC: O(h) h = height of the tree:
        if not root:
            return 0

        if not root.left and not root.right:
            return 1

        min_depth = float('inf')

        if root.left:
            min_depth = min(min_depth, self.minDepth(root.left))
        if root.right:
            min_depth = min(min_depth, self.minDepth(root.right))

        return min_depth + 1

root = build([1,2,2,3,None,None,3,4,None,None,4])
print(root)
solution = Solution1()
start_time = time.time()
print(solution.minDepth(root))
print("--- %s seconds ---" % (time.time() - start_time))