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

# Leetcode #144:
    # Note:
        # pre-order = Node, left, right
    # Idea:
        # traverse the root recursively
            # return [root.val] + left + right

class Solution1:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # recursive DFS:
        if not root:
            return []
        
        left = self.preorderTraversal(root.left)
        right = self.preorderTraversal(root.right)
        
        return [root.val] + left + right

class Solution2:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # iterative DFS:
        if not root:
            return []

        stack = [root]
        output = []

        while stack:
            node = stack.pop()

            if node:
                output.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        
        return output

root = build([1,None,2,3])
print(root)
solution = Solution1()
start_time = time.time()
print(solution.preorderTraversal(root))
print("--- %s seconds ---" % (time.time() - start_time))