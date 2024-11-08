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
class Solution1:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Note:
            # Post-order = Left -> Right -> Node
        # Idea:
            # traverse the root recursively/iteratively
                # recursive:
                    # return left + right + [root.val]
                # iterative:
                    # append node.left.val, node.right.val, then node.val

        # recursive DFS:
        if not root:
            return []

        left = self.postorderTraversal(root.left)
        right = self.postorderTraversal(root.right)

        return left + right + [root.val]

class Solution2:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # iterative DFS:
        if not root:
            return []

        stack = [root]
        output = []

        while stack:
            node = stack.pop()

            if node:
                output.append(node.val)
                stack.append(node.left)
                stack.append(node.right)

        return output[::-1]
                


root = build([1,None,2,3])
print(root)
solution = Solution2()
start_time = time.time()
print(solution.postorderTraversal(root))
print("--- %s seconds ---" % (time.time() - start_time))