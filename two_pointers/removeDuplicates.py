class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Objective:
            - given list of integers nums return k where k represents the number of unique elements in nums
            - removal must occur "in-place"
            - replaced value of the nums array could be any value

        Idea:
            1. using Set to store the visited element, if visited omit from counting
                - NOT AN IN-PLACE OPERATION
                - TC: O(n) / SC: O(n)
            2. sort the nums array, then use two pointers
                - TC: O(N log N) / SC: O(1) with .sort O(n) with .sorted
                - Problem states that the nums come sorted
                    - initialize l = 0
                    - iterate on nums (r = index) starting from 1
                        if nums[l] == nums[r]:
                            set nums[r] = _
                        else:
                            l += 1
                            nums[l], nums[r] = nums[r], nums[l]
                    - return l + 1
        """

        # TC: O(n) / SC: O(1)
        l = 0
        for r in range(1, len(nums), 1):
            if nums[l] == nums[r]:
                nums[r] = "_"
            else:
                l += 1
                nums[l], nums[r] = nums[r], nums[l]
        return l + 1
