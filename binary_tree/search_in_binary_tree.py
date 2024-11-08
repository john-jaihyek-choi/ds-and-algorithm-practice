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

# Leetcode #700
# idea:
            # traverse DFS with the condition:
                # if node.val == val:
                    # return node
                # elif node.val < val:
                    # traverse right of the node
                # else:
                    # traverse the left of the node

# Iterative DFS - TC O(log n) / SC: O(h)
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # iterative DFS:
        stack = [root]

        while stack:
            node = stack.pop()

            if node:
                if node.val == val:
                    return node
                if node.val < val:
                    stack.append(node.right)
                else:
                    stack.append(node.left)
        
    
# Recursive DFS - TC O(log n) / SC: O(h)
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # recursive DFS
        if not root:
            return root

        if root.val == val:
            return root
        elif root.val < val:
            return self.searchBST(root.right, val)
        else:
            return self.searchBST(root.left, val)
        

root = build([4,2,7,1,3])
print(root)
solution = Solution()
start_time = time.time()
print(solution.searchBST(root, 2))
print("--- %s seconds ---" % (time.time() - start_time))