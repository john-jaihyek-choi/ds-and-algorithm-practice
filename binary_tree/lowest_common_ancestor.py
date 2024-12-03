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
        # root of the the binary search tree to search on
    # p: TreeNode
        # node from the tree
    # q: TreeNode
        # node from the tree
    # constraints:
        # number of nodes in the tree will be greater than 2
        # -100 <= node.val <= 100
        # p != q
        # p and q will ALWAYS exists in the given tree
# output:
    # output: TreeNode
        # node.val of the Lowest Common Ancestor
# goal:
    # return an integer, node.val, of the node that is the lowest common ancestor of p and q 

# Brainstorm:
    # How do I know if the node at the current state of recursion is an LCA?
        # if node.left <= p and node.right >= q
            # Question1: is p guaranteed to be < q?
                # Assuming such constraint isn't in place:
                    # I'll have to handle the p and q comparison manually
                        # idea1: node.left <= min(p, q) and node.right >= max(p, q)
        # What if the above condition satifies?
            # return the current node.val
        # Should I use DFS or BFS?
            # DFS should be sufficient
        # Does order matter?
            # any order should be okay
                # Will take Post-order

class Solution:
    # Pseudocode:


    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
       


root1 = build([5,3,8,1,4,7,9,None,2])
p, q = 3, 8
print(root1)
print("p = ", p)
print("q = ", q)
solution = Solution()
start_time = time.time()
print(solution.lowestCommonAncestor(root1, p, q))
print("--- %s seconds ---" % (time.time() - start_time))