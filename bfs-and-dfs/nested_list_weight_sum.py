from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set
import time

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        The result is undefined if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        The result is undefined if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

"""
[NestedInteger{_integer: None, _list: [NestedInteger{_integer: 1, _list: []}, NestedInteger{_integer: 1, _list: []}]}, NestedInteger{_integer: 2, _list: []}, NestedInteger{_integer: None, _list: [NestedInteger{_integer: 1, _list: []}, NestedInteger{_integer: 1, _list: []}]}]
[]
"""


class Solution2:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        """
        Slight Space optimization by adding the total in-flight to remove the depth_index
        """

        # TC: O(n) / SC: O(n) for the callstack
        def dfs(nlist: List[NestedInteger], depth: int):  # TC: O(n)
            total = 0
            for item in nlist:
                if item.isInteger():
                    total += item.getInteger() * depth
                else:
                    total += dfs(item.getList(), depth + 1)

            return total

        return dfs(nestedList, 1)


class Solution1:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        """
        Note:
            - each list inside a list is depth + 1
            - outer most depth == 1
            - return the sum of all integers in each depth * the depth at which the integer is in
        Intuition:
            - initialize a depth index (defaultdict with list to hold list of integers)
                - each key representing depth
            - iterate on nestedList
                - start at depth 1
                - if nestedList[i] is integer:
                    - append the integer to depth_index[depth]
                - else:
                    - recurse
        """
        # TC: O(n) / SC: O(n)
        depth_index = defaultdict(list)  # SC: O(n)

        def dfs(nlist: List[NestedInteger], depth: int):  # TC: O(n)

            for item in nlist:
                integer = item._integer
                if integer is None:
                    dfs(item._list, depth + 1)
                else:
                    depth_index[depth].append(integer)

        dfs(nestedList, 1)

        return sum(key * sum(lst) for key, lst in depth_index.items())  # TC: O(d + n)


solution = Solution2()
start_time = time.time()
print(solution.depthSum([[1, 1], 2, [1, 1]]))
print("--- %s seconds ---" % (time.time() - start_time))
