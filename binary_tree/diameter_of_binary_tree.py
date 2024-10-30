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

class Solution:
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

root = build([1,2,2,3,None,None,3,4,None,None,4])
print(root)
solution = Solution()
start_time = time.time()
print(solution.diameterOfBinaryTree(root))
print("--- %s seconds ---" % (time.time() - start_time))