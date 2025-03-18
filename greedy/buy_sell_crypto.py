from collections import defaultdict
from typing import List, Dict, DefaultDict, Set
import time


class Solution3:
    def maxProfit(self, prices: List[int]) -> int:
        """
        # objective:
            # given array of prices, where prices[i] is the price of given stock on ith day, return the maximum procit one can achieve given the list of prices
        # keywords:
            # prices[i]:
                # price of the stock on the ith day
            # choose SINGLE day to buy one stock
            # choose different day in the future
            # find MAIMUM PROFIT obtainable
        # brainstorm:
            # bruteforce solution:
                # use nested loop to try and visit every pair
                # TC O(n^2) and inefficient
            # Optimal solution:
                # how can I eliminate visiting each pair of transactions
                    # what if I keep current min price?
                        # min starts at prices[0]
                        # then iterate on prices:
                            # compute profit and store in max_profit
                            # if n (current price) is less than min_price, update min_price
        # pseudocode:
            # min_price = prices[0]
            # max_profit = 0
            # for price in prices (price = prices[i])
                # max_profit = max(max_profit, price - min_price)
                # min_price = min(min_price, price)
            # return max_profit
        """

        # TC: O(n) / SC: O(1)
        min_price = prices[0]
        max_profit = 0
        for price in prices:
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)
        return max_profit


# reattempted at 3/4
class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        # input:
        # prices: List[int]
        # list of price at ith day
        # output:
        # output: int
        # goal:
        # given list of integers, return the maximum profit one can achieve
        # one can choose to buy at a single day and sell at another
        # one may choose not to make any transaction
        # idea:
        # bruteforce - check every possibility:
        # initialize max_profit at 0
        # iterate on prices (index = i)
        # iterate on prices at i + 1 (index = j)
        # max_profit = max(max_profit, prices[j] - prices[i])
        # optimization - keeping the current low:
        # initialize a current low value at max(prices)
        # iterate on prices (price = prices[i])
        # set max_profit to max(max_profit, price - current_low)
        # set current_low to min(current_low, price)
        # return max_profit

        # Bruteforce pseudocode:
        # max_profit = 0
        # for i in range(len(prices)):
        # for j in range(i + 1, len(prices), 1):
        # max_profit = max(max_profit, prices[j] - prices[i])
        # return max_profit

        # TC: O(n^2) / SC: O(1)
        max_profit = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices), 1):
                max_profit = max(max_profit, prices[j] - prices[i])

        return max_profit

        # Optimized pseudocode:
        # current_low = max(prices)
        # max_profit = 0
        # for price in prices:
        # max_profit = max(max_profit, price - current_low)
        # current_low = min(current_low, price)
        # return max_profit

        # TC: O(n) / SC: O(1)
        current_low = max(prices)
        max_profit = 0

        for price in prices:
            max_profit = max(max_profit, price - current_low)
            current_low = min(current_low, price)

        return max_profit


class Solution1:
    def maxProfit(prices: List[int]) -> int:
        # Note:
        # prices[i] is the price at ith day
        # output must be the value of the maximum profit you can make

        # Brainstorm:
        # while future value at i is less than the current value i, we need to check the next immediate future value
        # if all current values are less than the future value, then we return 0
        # How to maximize profit:
        # 1. make sure prices[r] > prices[l]
        # 2. buy at the smallest value and sell at the maximum value
        # What the essential piece of information?
        # lowest price
        # When a new lowest price is found, the total max profit should reset to calculate the temporary max profit

        # Pseudocode:
        # initialize the max_profit variable = 0
        # initialize lowest_price at first value in prices array
        # initialize l and r where:
        # l = 0
        # r = l + 1
        # iterate the prices array while r < length of the array:
        # check if prices[r] < lowest_price:
        # if true, lowest_price = prices[r] and set l to position of r, and r to position of r + 1
        # set max_profit to maximum value of max_profit and temp_profit
        # else, add the difference of prices[r] - prices[l] to max_profit

        # Solution 1 (Bruteforce - TC: O(n^2) SC: O(1)):
        max_profit = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                max_profit = max(max_profit, (prices[j] - prices[i]))

        return max(0, max_profit)

        max_profit, l, r = 0, 0, len(prices) - 1
        lowest_price = min(prices[l], prices[r])

        while l < r:
            max_profit = max(max_profit, prices[r] - prices[l])

            if prices[l + 1] - prices[l] <= prices[r] - prices[r - 1]:
                l += 1
            else:
                r -= 1

        return max(0, max_profit)

        # Solution 2 (TC: O(n) SC: O(1))
        max_profit, lowest_price = 0, prices[0]
        l, r = 0, 1
        profit = 0

        while r < len(prices):
            if prices[r] <= lowest_price:
                lowest_price = prices[r]
                profit = 0

                l = r
                r = l + 1
            else:
                profit += prices[r] - prices[r - 1]
                r += 1

            max_profit = max(max_profit, profit)

        return max_profit

        # Solution 3 (TC: O(n) SC: O(1) Cleaner Version)
        max_profit = 0
        l, r = 0, 1

        while r < len(prices):
            if prices[l] <= prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            else:
                l = r
            r += 1

        return max_profit

        # Solution 4 (TC: O(n) SC: O(1) Cleaner Version)
        max_profit = 0

        lowest = 0
        for price in prices:
            if price <= lowest:
                lowest = price
            max_profit = max(max_profit, price - lowest)
        return max_profit

        # Solution 5 - Another variation of Solution 4 (TC: O(n) SC: O(1))
        profit = 0
        lowest = prices[0]

        for price in prices:
            lowest = min(lowest, price)
            profit = max(profit, price - lowest)
        return profit


start_time = time.time()
solution = Solution3()
print(solution.maxProfit([7, 1, 5, 3, 6, 4]))
print("--- %s seconds ---" % (time.time() - start_time))
