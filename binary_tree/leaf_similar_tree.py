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

# Leetcode 872:
# Cleaner/Optimal approach (list concatenation):
# TC: O(n + m) / SC: O(h1 + h2)
class Solution2:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        return self.dfs(root1) == self.dfs(root2)

    def dfs(self, root: Optional[TreeNode]) -> List[int | None]:
        if not root:
            return []

        left = self.dfs(root.left)
        right = self.dfs(root.right)

        if not left and not right:
            return [root.val]
        
        return left + right

# Initial attempt:
# TC: O(n + m) / SC: O(h1 + h2)
class Solution1:
    def __init__(self):
        self.root1_leaves = []
        self.root2_leaves = []

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        self.dfs(root1, self.root1_leaves)
        self.dfs(root2, self.root2_leaves)

        return self.root1_leaves == self.root2_leaves

    def dfs(self, root: Optional[TreeNode], leaves_arr: List[int]) -> bool:
        if not root:
            return False

        left = self.dfs(root.left, leaves_arr)
        right = self.dfs(root.right, leaves_arr)

        if not left and not right:
            leaves_arr.append(root.val)
        
        return True

root1 = build([3,5,1,6,2,9,8,None,None,7,4])
root2 = build([3,5,1,6,7,4,2,None,None,None,None,None,None,9,8])
print(root1)
print(root2)
solution = Solution2()
start_time = time.time()
print(solution.leafSimilar(root1, root2))
print("--- %s seconds ---" % (time.time() - start_time))