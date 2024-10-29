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

# Iterative DFS Approach: use of stack per layer
class Solution3:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        layer = 0
        stack = [[root, 1]]

        while stack:
            node, new_layer = stack.pop()
            if node:
                layer = max(layer, new_layer)
                stack.append([node.right, new_layer + 1])
                stack.append([node.left, new_layer + 1])
        
        return layer

# Iterative BFS: use deque to keep track of left and right nodes in the tree
class Solution2:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        layer = 0
        q = deque([root])
        while q:
            # take snapshot of q len, then iterate len(q) many times to pop items for given layer (breadth)
            for _ in range(len(q)):
                # node will contain popped node
                node = q.popleft()
                # check if popped node have left value
                if node.left:
                    q.append(node.left)
                # check if popped node have right value
                if node.right:
                    q.append(node.right)

            # when done with layer iteration, increase layer
            layer += 1
        
        return layer

# recursive DFS:
class Solution1:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # base case:
            # if root is None:
                # return 0
        # else:
            # set left depth
            # set right depth
            # return bigger of the two depths

        # TC: O(n) / SC: O(1) but O(h) for implicit call stack
        if not root:
            return 0
        
        left = self.maxDepth(root.left) + 1
        right = self.maxDepth(root.right) + 1

        return max(left, right)

root = build([1,2,2,3,None,None,3,4,None,None,4])
print(root)
solution = Solution3()
start_time = time.time()
print(solution.maxDepth(root))
print("--- %s seconds ---" % (time.time() - start_time))