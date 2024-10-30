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

# Optimal solution:
# TC: O(n) / SC: O(h)
class Solution2:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # note:
            # In order for a tree to be balanced:
                # the difference between the left and the right height must be no greater than 1
        # Brainstorm:
            # what is needed?
                # the height at left and right is needed
            # what do I need to process?
                # get the bigger of the left or the right height and return to its parent (with +1)
                # This gives the total max left and max right heights
            # compute the difference of the left and the right height
        if not root:
            return True

        res = self.height_dfs(root)

        return res[1]

    def height_dfs(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return [0, True]
        
        left_h, left_isBalanced = self.height_dfs(root.left)
        right_h, right_isBalanced = self.height_dfs(root.right)

        height = max(left_h, right_h)
        isBalanced = abs(left_h - right_h) <= 1 and left_isBalanced and right_isBalanced

        return [height + 1, isBalanced]
    
# Bruteforce
# TC: O(n^2) / SC: O(h)
class Solution1:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # check if height conditions satisfy
            # check if the node is balanced
        if not root:
            return True

        left_h = self.check_height(root.left)
        right_h = self.check_height(root.right)
        
        if abs(left_h - right_h) > 1:
            return False

        left_balanced = self.isBalanced(root.left)
        right_balanced = self.isBalanced(root.right)

        return left_balanced and right_balanced
        

    def check_height(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return 0

        left = self.check_height(root.left)
        right = self.check_height(root.right)
        
        return max(left,right) + 1

root = build([1,2,2,3,None,None,3,4,None,None,4])
print(root)
solution = Solution2()
start_time = time.time()
print(solution.isBalanced(root))
print("--- %s seconds ---" % (time.time() - start_time))