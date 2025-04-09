class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Objective: given list of integers, return k where k is the number of elements in array after removing elements that are equal to val

        Ideas:
            1. Bruteforce: iterate on nums, replace nums[i] to _ if equal to 3, then return the sorted nums
                - TC: O(N log N) / SC: O(1) if .sort, O(n) if .sorted()
            2. Two-pointers: use two pointers starting at each end, then replace if nums[l] != val
                - initialize l, r = 0, len(nums) - 1
                - while l <= r:
                    - if nums[l] == val:
                        - nums[l], nums[r] = nums[r], "_"
                        - decrement r by 1
                    - else:
                        increment l by 1
        """

        # TC: O(n) / SC: O(1)
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] == val:
                nums[l], nums[r] = nums[r], "_"
                r -= 1
            else:
                l += 1

        return l
