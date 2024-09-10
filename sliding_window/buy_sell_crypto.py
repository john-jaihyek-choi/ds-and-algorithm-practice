from collections import defaultdict
from typing import List, Dict, DefaultDict, Set
import time

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
            


    # Solution 1 (Bruteforce):
    # max_profit = 0
    # for i in range(len(prices)):
    #     for j in range(i+1, len(prices)):
    #         max_profit = max(max_profit, (prices[j] - prices[i]))

    # return max(0, max_profit)

    # max_profit, l, r = 0, 0, len(prices) - 1
    # lowest_price = min(prices[l], prices[r])

    # while l < r:
    #     max_profit = max(max_profit, prices[r] - prices[l])

    #     if prices[l + 1] - prices[l] <= prices[r] - prices[r - 1]:
    #         l += 1
    #     else:
    #         r -= 1

    # return max(0, max_profit)

    max_profit, lowest_price = 0, prices[0]
    l, r = 0, 1
    profit = 0
    
    while(r < len(prices)):
        if prices[r] <= lowest_price:
            lowest_price = prices[r]
            profit = 0
            
            l = r
            r = l + 1
        else:
            profit += prices[r] - prices[r-1]
            r += 1

        max_profit = max(max_profit, profit)

    return max_profit

start_time = time.time()
print(maxProfit([7,1,5,3,6,4]))
print("--- %s seconds ---" % (time.time() - start_time))