from collections import defaultdict
from typing import List
from helper.functions import TreeNode
from typing import Optional
import time
from binarytree import build

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # recursive:
        # base case:
            # if root not valid:
                # return head
        # else:
            # switch left with right:
            # traverse the left and right of the tree
        
        # TC: O(n) / SC: O(1) but O(h) where h = max height of the tree for implicit call stack
        if not root:
            return None
        
        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


root = build([1,2,3,4,5,6,7])
print(root)
solution = Solution()
start_time = time.time()
print(solution.invertTree(root))
print("--- %s seconds ---" % (time.time() - start_time))