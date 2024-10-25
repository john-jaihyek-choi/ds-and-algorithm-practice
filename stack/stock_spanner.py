from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set
from operator import add, sub, mul, truediv
import time

# Leetcode 901
class StockSpanner:
    # goal:
        # implement a class StockSpanner which keeps track of history of the stock prices
            # comes with 1 method called next
                # the next method get today's stock price as an argument
                    # returns the span where the stock price was less than or equal to today's price.
                        # ex) days:  1,  2,  3,   4,   and today_price = 3
                        #           [4,  1,  2,   1]
                        #                            span = 4 because today's price = 3 and the consecutive previous stock prices are less than or equal to today's price
                # the next method should return the span of days where the stock price was <= today's price

    def __init__(self):
        # initialize stock_prices
            # stock_prices: List[Tuple[int, int]]
                # Tuple[0] = stock price
                # Tuple[1] = span
                # initialize with empty array
            # the stock_prices must be in a monotonic decresing behavior
        self.stock_prices = []

    def next(self, price: int) -> int:
        # bruteforce:
        # span = 1
        # for i in range(len(self.stock_prices) - 1, -1, -1):
        #     if self.stock_prices[i] <= price:
        #         span += 1
        #     else:
        #         break
        # self.stock_prices.append(price)
        # return span

        # initialize a span counter at 1
        # while self.stock_prices and self.stock_prices[-1] is less than or equal to price
        #     pop the stock_prices
        #     increment a span counter
        # append the price to stock_price
        # return the span counter
        res = 1
        while self.stock_prices and self.stock_prices[-1][0] <= price:
            previous_price, span = self.stock_prices.pop()
            res += span
        self.stock_prices.append(tuple([price, res]))
        return res


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

start_time = time.time()
print("--- %s seconds ---" % (time.time() - start_time))