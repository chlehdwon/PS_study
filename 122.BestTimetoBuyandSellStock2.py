"""
Say you have an array prices for which the ith element is the price of
a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as
many transactions as you like (i.e., buy one and sell one share of the
stock multiple times).

Note: You may not engage in multiple transactions at the same time
(i.e., you must sell the stock before you buy again).
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        profit, buy = 0, False
        for i in range(len(prices)-1):
            if not buy and prices[i] < prices[i+1]:
                profit -= prices[i]
                buy = True
            elif buy and prices[i] > prices[i+1]:
                profit += prices[i]
                buy = False
        if buy:
            profit += prices[-1]
        return profit


class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        profit = 0
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                profit += prices[i+1] - prices[i]

        return profit


class Solution3:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(max(prices[i+1]-prices[i], 0) for i in range(len(prices) - 1))


# Implementation by using DP
class Solution4:
    def maxProfit(self, prices) -> int:
        # It is impossible to sell stock on first day, set -infinity as initial value for cur_hold
        # cur_hold : my money when we buy stock 
        # cur_not_hold : my money when we sell stock
        cur_hold, cur_not_hold = -float('inf'), 0
        for stock_price in prices:
            prev_hold, prev_not_hold = cur_hold, cur_not_hold
            # either keep hold, or buy in stock today at stock price
            cur_hold = max( prev_hold, prev_not_hold - stock_price )
            # either keep not-hold, or sell out stock today at stock price
            cur_not_hold = max( prev_not_hold, prev_hold + stock_price )
            print(cur_hold, cur_not_hold)
        # maximum profit must be in not-hold state
        return cur_not_hold if prices else 0


a = Solution3()
print(a.maxProfit([7,1,5,3,6,4]))
