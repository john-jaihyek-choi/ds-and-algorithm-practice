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


class Solution2:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Optimization with left and right most col variables
        """

        # TC: O(n) / SC: O(n)
        output = []  # SC: O(n)
        if root is None:
            return output

        q = deque([(root, 0)])  # SC: O(n)
        columns = defaultdict(list)  # SC: O(n)
        left_most_col, right_most_col = float("inf"), float("-inf")

        while q:  # TC: O(n)
            for _ in range(len(q)):
                node, col = q.popleft()
                columns[col].append(node.val)
                left_most_col = min(left_most_col, col)
                right_most_col = max(right_most_col, col)

                if node.left:
                    q.append((node.left, col - 1))
                if node.right:
                    q.append((node.right, col + 1))

        return [
            columns[col] for col in range(left_most_col, right_most_col + 1)
        ]  # TC: O(n)


class Solution1:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Note:
            - return vertical order traversal of nodes value
                - left to right
                - top to bottom
        Intuition:
            - BFS
                - traverse the tree with BFS
                    - starting at root node as column 0
                    - add each layer to queue and store each node value and column value to dictionary:
                        - add left node with current node's column - 1
                        - add right node with current node's column + 1
                - sort the dictionary by column (key) in increasing order
                - iterate and return the node values for the output
        """

        # TC: O(n log n) / SC: O(n)
        output = []  # SC: O(n)
        if root is None:
            return output

        q = deque([(root, 0)])  # SC: O(n)
        columns = defaultdict(list)  # SC: O(n)

        while q:  # TC: O(n)
            for _ in range(len(q)):
                node, col = q.popleft()
                columns[col].append(node.val)

                if node.left:
                    q.append((node.left, col - 1))
                if node.right:
                    q.append((node.right, col + 1))

        sorted_columns = sorted(columns.items(), key=lambda x: x[0])  # TC: O(n log n)

        return [item[1] for item in sorted_columns]  # TC: O(n)


solution = Solution2()
start_time = time.time()
print(solution.verticalOrder([3, 9, 20, None, None, 15, 7]))
print("--- %s seconds ---" % (time.time() - start_time))
