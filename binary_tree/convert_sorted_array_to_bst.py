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

# Leetcode #108
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # Note:
            # In an ascending sorted array, the the value at the mid index is the root of the entire array
            # repeat this for the left half and right half recursively
        
        # TC: O(n) / SC: O(n)
        if not nums:
            return None

        mid = len(nums) // 2

        root = TreeNode(nums[mid])

        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])

        return root
        

solution = Solution()
start_time = time.time()
print(solution.sortedArrayToBST([-10,-3,0,5,9]))
print("--- %s seconds ---" % (time.time() - start_time))