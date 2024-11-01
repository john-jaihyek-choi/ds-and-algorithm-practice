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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # recursive DFS:
            # recurse until leaf node
                # check the sum with target

        return self.target_found(root, targetSum, 0)

    def target_found(self, root: Optional[TreeNode], target: int, sum_val: int) -> bool:
        if not root:
            return False

        current_sum = root.val + sum_val
        print(current_sum)
        if not root.left and not root.right:
            return current_sum == target

        return (self.target_found(root.left, target, current_sum) or
                self.target_found(root.right, target, current_sum))

root = build([5,4,8,11,None,13,4,7,2,None,None,None,1])
print(root)
solution = Solution()
start_time = time.time()
print(solution.hasPathSum(root, 22))
print("--- %s seconds ---" % (time.time() - start_time))