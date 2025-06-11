import random


class Solution2:

    def __init__(self, w: List[int]):
        self.prefix_sums = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)
        self.weight_sum = prefix_sum

    def pickIndex(self) -> int:
        """
        Note:
            - Index Picking Probability:
                - w[i] / sum(w)
            - Radomly pick index in the range [0, len(w) - 1]
        """
        target = self.weight_sum * random.random()

        return self.search(0, len(self.prefix_sums) - 1, target)

    def search(self, start: int, end: int, target: float) -> int:
        l, r = start, end

        while l < r:
            m = (r + l) // 2
            if target > self.prefix_sums[m]:
                l = m + 1
            else:
                r = m

        return l


class Solution1:

    def __init__(self, w: List[int]):
        self.prefix_sums = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)
        self.weight_sum = prefix_sum

    def pickIndex(self) -> int:
        """
        Note:
            - Index Picking Probability:
                - w[i] / sum(w)
            - Radomly pick index in the range [0, len(w) - 1]
        """
        target = self.weight_sum * random.random()

        for i, p_sum in enumerate(self.prefix_sums):
            if target < p_sum:
                return i


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
