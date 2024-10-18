from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set
import time

class Solution4:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # input:
            # nums: List[int]
            # k: int
                # size of the window
        # goal: return a list that contains the maximum element in the window at each step
        # Sliding window approach:
            # main challenge of the problem:
                # how to know the maximum within the window boundary
            # l and r
                # when to move l?
                    # l moves when r has reached k
                        # when r >= k, l moves
                # when to move r?
                    # every iteration
            # how do I track max value within the boundary?
                # as r and l moves, store the max within the boundary
                    # how?
                        # using stack or queue?
                            # won't work since stack can't pop the bottom. It's one way pop
                        # double ended queue?
                            # double ended queue can pop and append from each end of the list O(1)
                    # How can I properly store the max?
                        # if we keep the deque in a strictly decreasing order, we can ensure we have access to max in O(1) tine
                        # if value at the top of the deque is greater than the one appending, append.
                        # if value at the top of the dque is less than the one appending, pop until top of the stack is greater, then append
                    # But how do I keep track of max within boundary in each iteration?
                        # since l pointer represents an index of the number
                            # storing index to the number can ensure that we can pop the bottom of the stack (max) when out of bounds
                                # when l > stack[0]
                            # even if the bottom is popped, the next number will be guaranteed to be a max value
            # return value?
                # need to return a max value at each index in each slide
            # Variables to track:
                # res: List[int]
                # l and r pointer
                    # l: int
                    # r: int
                # q: Deque[]
            
            # Pseudocode:
                # initialize an empty deque (deque)
                # initialize an empty array for response (res)
                # initialize an l pointer to 0
                # loop nums (r = index, n = nums[r])
                    # while q is valid and value of nums[q[-1]] < n:
                        # pop the top of the q
                    # append r to the q
                    # if r >= k:
                        # if l > q[0]:
                            # q.popleft()
                        # increment l by 1
                        # res.append(nums[q[0]])
            
        q, res = deque(), []
        l = 0
        for r, n in enumerate(nums):
            while q and nums[q[-1]] < n:
                q.pop()
            
            q.append(r)

            if r + 1 >= k:
                if l > q[0]:
                    q.popleft()
                
                l += 1
                res.append(nums[q[0]])
                
            
        return res

class Solution3:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Solution 3 (TC: O(n) / SC: O(k + n) if includes res_output):
        res_output = [] # SC: O(n)
        q = deque() # SC: O(k)
        l = 0
        
        for r in range(len(nums)): # TC: O(n)
            while q and nums[r] > nums[q[-1]]: # TC: O(k)
                q.pop() # TC: O(1)
            q.append(r) # TC: O(1)

            # if new l we are shifting is bigger than the q[0] (index of the current max in the window)
            if l > q[0]: # TC: O(1)
                q.popleft() # TC: O(1)

            if r + 1 >= k: # TC: O(1)
                res_output.append(nums[q[0]]) # TC: O(1)
                l += 1 # TC: O(1)

        return res_output


class Solution2:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    # Solution 2:
        # Brainstorm:
            # Main problems of bruteforce solution that are causing O(k * (n - k))
                # Max function - O(k) operation to find max of a substring
                # Substring retrieval (ex: nums[l:r])
            # What are some parts of a window within a loop we have O(1) access to?
                # where:
                    # l is the left edge of the window
                    # r is the right edge of the window
                # 1. nums[l] and nums[r] are O(1) access
                # 2. l and r is directly accessible
            # Summary:
                # In order to search for a max value, the operation inside a loop would be O(k) repeatedly
                # And this is expensive because we are potentially revisting the elements we've visited in the prior window
            # Use of Deque:
                #  Deque is a data structure which has the benefit of list, but with couple more advantages when it comes to accessing/removing an index:
                    # append and appendleft - O(1) operation
                    # pop and popleft - O(1) operation
                # if Deque is used, I can keep the deque in an always decreasing order by popping the elements that are in the left most queue if smaller than the incoming number from the new window
        # Pseudocode:
            # if the length of the input nums list is less than input k, return the max of nums array
            # initialize an empty deque (q)
            # initialize the l pointer at 0
            # iterate the nums array (r = index)
                # if nums[r] is greater than q[0]
                    # append the nums[r] to the q from the left
                # if r < k
                    # append nums[r] to the queue
                    # 
        if len(nums) < k:
            return max(nums)
        elif k == 1:
            return nums
        
        output = []
        q = deque()
        l = 0

        for r in range(len(nums)): # O(n)
            # if q is non-empty AND the value in q[-1] (current minimum) is greater than nums[r], pop the q, then append the nums[r]
            while q and nums[q[-1]] < nums[r]: # O(1)
                q.pop() # O(1)
            q.append(r) # O(1)
            
            # if the current max is out of bounds (less than l), pop the q from the left to remove the max
            if l > q[0]: # O(1)
                q.popleft() # O(1)

            # if r - l + 1 (size of the window) has reached k, then start incrementing l pointer
            if r - l + 1 >= k:
                output.append(nums[q[0]]) # O(1)
                l += 1
            
        return output

class InvalidSolution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    # INVALID SOLUTION
        # Brainstorm:
        # Main problems of bruteforce solution that are causing O(k * (n - k))
            # Max function - O(n) operation to find max of a substring
            # Substring retrieval (ex: nums[l:r])
        # What are some parts of a window within a loop we have O(1) access to?
            # where:
                # l is the left edge of the window
                # r is the right edge of the window
            # 1. nums[l] and nums[r] are O(1) access
            # 2. l and r is directly accessible
        # at point L and R, how do we know what is the max value within the given window?
            # Can we tell somehow by looking at nums[L] and nums[R] to determine if there's bigger value contained between it?
                # Logically:
                    # if nums[L] and nums[R] is smaller than whatever the value is between it, the max value between the L and R window is the max value
                    # if nums[L] is greater than nums[R], then nums[L] is the max value
                    # if nums[R] is greater than nums[L], then nums[R] is the max value
            # If we store the left and right max boundary at each given nums[i], then we know exactly what the maximum is with respect to nums[L] and nums[R]
                # ex)
                #  nums  = [  1,  6,  4,  2,  7, 10,  2,  0,  1 ] where k = 3
                #  l_max = [  1,  6,  6,  6,  7, 10, 10, 10, 10 ] max value (including value at i) with respect to values to the left of i
                #  r_max = [ 10, 10, 10, 10, 10, 10,  2,  1,  1 ] max value (including value at i) with respect to values to the right of i
                    # *** NOTE ***
                    # It won't be possible to achieve O(n) as easy as l_max because we need to iterate from the back of the array to 0
                        # In the process, the order in which the right max values get stored in will be reversed
                            # We can use built in sort, but it will be O(n log n)
                        # ** Workaround **
                            # instead of generating r_max, we can start the window to search from the end of the nums array instead of going from 0
                #  output = [ 6, 6, 7, 10, 10, 10, 2]
            # Given the above pattern, we can derive the max value within the L and R by taking the min of l_max[r] and r_max[l]
                # If put in words:
                    # l_max[r] is the largest number at nums[r] with respect to all values to the left of it
                    # r_max[l] is the largest number at nums[l] with respect to all values to the right of it
                    # Visualization:
                        # If l_max[r] = 10 and l_max[r] = 6
                            #   0    1     2     3     4  5  6  7  8
                            #     r_max[l] = 10 -> means the biggest value to the right of it is 10     
                            # [ ?,   6,    ?,    2,    ?, ?, ?, ?, ? ]
                            #                  l_max[r] = 6 -> means the biggest value to the left of it is 6
                        # Based on the above, logic above - since l_max[r] value is 6, we know for sure that any value between 6 and 2 could only ever be 6
        # *** Flaw with the solution ***:
            # When combining the min of the maximums using min(l_max[r], r_max[l]), I'm not necessarily getting the maximum for each sliding window. Instead, I'm computing the minimum of the maximums, which isn't the desired outcome.
                # For each sliding window of size k, I must find the maximum element in that window.
        # Pseudocode:
            # initialize an empty array to store the result (output)
            # initialize l_max list to store the maximum values with respect to nums[i]'s left values (l_max)
            # initialize r_max list to store the maximum values with respect to nums[i]'s right values (r_max)
                # initialize it to empty array with 0s with length of nums
            # set maximum = 0
            # iterate nums array starting from 0
                # compute the maximum
                # collect left max values with respect to nums[i]
            # set maximum = nums[-1]
            # iterate nums array again starting from the end of the array
                # compute the maximum
                # collect right max values with respect to nums[i]
            # initialize the l pointer at 0 (l)
            # iterate the nums array starting at k until the end of the array (r = current index)
                # append the smaller value between l_max[r] and r_max[l] to the output array
                # increment the l by 1

        # INVALID SOLUTION
        if k == 1:
            return nums
        
        output, l_max = [], []
        r_max = [0] * len(nums)

        maximum = 0
        for num in nums:
            maximum = max(maximum, num)
            l_max.append(maximum)

        maximum = nums[-1]
        for i in range(len(nums) - 1, -1, -1):
            maximum = max(maximum, nums[i])
            r_max[i] = maximum

        l = 0
        for r in range(k - 1, len(nums)):
            output.append(min(l_max[r], r_max[l]))
            l += 1

        return output

class Solution1:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Solution 1 Bruteforce (TC: O(k * (n - k)) / SC: O(n)) 
        output = []
        l = 0

        for r in range(k, len(nums) + 1): # O(n - k)
            output.append(max(nums[l:r])) # O(k) + O(k)
            l+=1

        return output


solution = Solution4()
start_time = time.time()
print(solution.maxSlidingWindow([1,3,1,2,0,5], 3))
print("--- %s seconds ---" % (time.time() - start_time))
