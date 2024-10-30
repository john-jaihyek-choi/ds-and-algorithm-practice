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
    # p: TreeNode || None
        # root of the first tree
    # q: TreeNode || None
        # root of the second tree
# goal:
    # return boolean:
        # True if p and q are same
        # False otherwise
    # trees are "same" if the values and the order of the nodes are the same.
# Brainstorm:
    # Bruteforce Idea:
        # iterate on root1 and and root2, then collect the nodes in 2 set of arrays
        # compare the 2 arrays if identical

# Optimal approach - 2nd Try:
# Early termination without going through every nodes
# TC: O(n + m) / SC: O(n + m)
class Solution3:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            # traversal will stop when neither of the traversal returns False
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False

# Optimal approach - 1st Try:
# TC: O(n + m) / SC: O(h1 + h2) for the call stack
class Solution2:
    # Optimization Idea:
        # is there an opportunity traverse and check each nodes in-place?
            # for example - checking the 2 roots if they are equal
                # if equal:
                    # traverse the left node
                    # traverse the right node
                # else:
                    # return false
            # What should the order of the process be like?
                # Pre-order
                    # 1. Check root
                    # 2. traverse left (or right)
                    # 3. traverse right (or left)


    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if (p and q) and p.val == q.val:
            left = self.isSameTree(p.left, q.left) 
            right = self.isSameTree(p.right, q.right)
            return left and right
        else:
            return False


# Initial Try:
# TC: O(n + m) / SC: O(n + m)
class Solution1:
    # Pseudocode (Bruteforce):
    # Create a separate method that traverses and copies the node.val to the array (dfs)
        # input:
            # root: TreeNode | None
        # output:
            # List[int | None]
        # base case:
            # if not root:
                # return []
            # traverse left node
                # left = self.dfs(root.left)
            # traverse right node
                # right = self.dfs(root.right)
            # return left + right + [root.val]
    # from the isSameTree method, call the dfs method on root1 and root2:
        # return self.dfs(p) == self.dfs(q)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.dfs(p) == self.dfs(q)
    
    def dfs(self, root: Optional[TreeNode]) -> List[int | None]:
        if not root:
            return ['Null']
        
        left = self.dfs(root.left)
        right = self.dfs(root.right)

        return left + right + [root.val]


root1 = build([4, 7])
root2 = build([4, None, 7])
print(root1)
print(root2)
solution = Solution2()
start_time = time.time()
print(solution.isSameTree(root1, root2))
print("--- %s seconds ---" % (time.time() - start_time))