from collections import defaultdict
from typing import List
from helper.functions import TreeNode
from typing import Optional
import time

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


solution = Solution()
start_time = time.time()
print(solution.invertTree(["mobile", "mouse", "moneypot", "monitor", "mousepad"], "mouse"))
print("--- %s seconds ---" % (time.time() - start_time))