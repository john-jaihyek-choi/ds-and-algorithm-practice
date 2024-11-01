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

# Optimal Iterative method (TC: O(n) / SC: O(n))
class Solution3:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # iteratively
        if not root:
            return True

        queue = deque([(root.left, root.right)])

        while queue:
            left, right = queue.popleft()

            if not left and not right:
                continue
                
            if not left or not right or left.val != right.val:
                return False
            
            queue.append((left.left, right.right))
            queue.append((left.right, right.left))
                
        return True

# Optimal Recursive method (TC: O(n) / SC: O(h)):
class Solution2:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.isMirror(root.left, root.right)

    def isMirror(self, node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
        if not node1 and not node2:
            return True
        if not node1 or not node2:
            return False
        return (node1.val == node2.val 
                and self.isMirror(node1.left, node2.right) 
                and self.isMirror(node1.right, node2.left))


# Fist Try:
class Solution1:
    # Brainstorm - Recursive (TC: O(n) / SC: O(h)):
    # traverse on one side, left or right (O(n))
        # invert the tree
    # compare if root.right is same tree with inverted tree

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # recursive:
        if not root: # O(1)
            return True
        
        inverted_left = self.invertTree(root.left) # O(n)
        
        return self.isSameTree(inverted_left, root.right) # O(n)

        
    def isSameTree(self, t1: Optional[TreeNode], t2) -> bool:
        if not t1 and not t2:
            return True
        if t1 and t2 and t1.val == t2.val:
            return self.isSameTree(t1.left, t2.left) and self.isSameTree(t1.right, t2.right)
        else:
            return False

    def invertTree(self, root: Optional[TreeNode]) -> TreeNode:
        if not root:
            return None
        
        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root



root = build([1,2,3,4,5,None,8,None,None, 6,7, None, None, 9])
print(root)
solution = Solution1()
start_time = time.time()
print(solution.isSymmetric(root))
print("--- %s seconds ---" % (time.time() - start_time))