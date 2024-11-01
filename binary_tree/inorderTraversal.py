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
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # recursive method:
        # if not root:
        #     return []
        
        # left = self.inorderTraversal(root.left)
        # right = self.inorderTraversal(root.right)

        # return left + [root.val] + right

        # iterative method:
        stack = []
        current = root
        output = []
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            
            current = stack.pop()
            output.append(current.val)
                
            current = current.right

        return output


root = build([1,2,3,4,5,None,8,None,None, 6,7, None, None, 9])
print(root)
solution = Solution()
start_time = time.time()
print(solution.inorderTraversal(root))
print("--- %s seconds ---" % (time.time() - start_time))