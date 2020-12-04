# Say you have an array prices for which the ith element is the price
# of a given stock on day i.

# Design an algorithm to find the maximum profit. You may complete as
# many transactions as you like (i.e., buy one and sell one share of 
# the stock multiple times)

# My answer
class Solution:
    def maxProfit(self, prices):
        maxprofit = 0
        buy, sell = prices[0], prices[0]
        for p in prices[1:]:
            if p > sell:
                sell = p
            else:
                maxprofit += sell - buy
                buy, sell = p, p
        maxprofit += sell - buy
        return maxprofit


#More Faster Version. Basic Algorithm is same as my answer. 
class Solution2:
    def maxProfit(self, prices) -> int:
        
        profit_from_price_gain = 0
        for idx in range( len(prices)-1 ):
            
            if prices[idx] < prices[idx+1]:
                profit_from_price_gain += ( prices[idx+1] - prices[idx])
                
        return profit_from_price_gain


# Implementation by using DP
class Solution3:
    def maxProfit(self, prices) -> int:
        # It is impossible to sell stock on first day, set -infinity as initial value for cur_hold
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
