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

# input:
    # root: TreeNode
    # subRoot: TreeNode
# output:
    # output: boolean
# goal:
    # return boolean:
        # True if:
            # root contains subtree that matches subRoot's structure and the values
        # False otherwise:
    # subRoot is identical to subtree of tree that consists of a node in tree and all of its node's descendants
# Note:
    # subtree of the root that's similar in structure with subroot MUST have identical children nodes' structure and values
        # if subtree only contains part of the subroot and not the complete subroot, the subroot is NOT a subtree

# Bruteforce:
# TC: O(n * m) / SC: O(h1 + h2)
class Solution:   
    # Brainstorm:
        # Bruteforce:
            # check at each node if the tree starting at root is the same with subroot
                # if true:
                    # return True
                # if false:
                    # continue traversing
    # Pseudocode:
        # 1. traverse the node:
            # if root.val == subroot.val:
                # check if the tree is the same as subroot (step 2)
                    # if True:
                        # return True
                    # otherwise:
                        # continue traversing
            # traverse the left node
            # traverse the right node
        # 2. check if the tree at its current state's root is same with subroot
            # base conditions:
                # if not root and not subroot:
                    # return True
                # if not root or not subroot:
                    # return False
                # if root.val != subRoot.val:
                    # return False
                # else:
                    # traverse to the left and the right node to continue comparing
                        # return dfs(root.left, subRoot.left) and dfs(root.right, subRoot.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        
        if not root:
            return False

        if root.val == subRoot.val and self.compare_trees(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def compare_trees(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> None:
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        if root.val != subRoot.val:
            return False

        return self.compare_trees(root.left, subRoot.left) and self.compare_trees(root.right, subRoot.right)

root1 = build([3,4,5,1,2,None,None,None,None,0])
root2 = build([4,1,2])
print(root1)
print(root2)
solution = Solution()
start_time = time.time()
print(solution.isSubtree(root1, root2))
print("--- %s seconds ---" % (time.time() - start_time))