# Say you have an array for which the ith element is the price of
# a given stock on day i.

# If you were only permitted to complete at most one transaction
# (i.e., buy one and sell one share of the stock),
# design an algorithm to find the maximum profit.

# Note that you cannot sell a stock before you buy one.


# Dynamic Programming Solution. 
# For prices list for index 0 to index i,
# We put -(the cost of stock when we buy) at dp[i][0]
# And the maximum profit at dp[i][1]

class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        dp = [[0] * 2 for _ in range(n + 1)]
        dp[0][0] = float('-inf')
        for i, p in enumerate(prices, 1):
            dp[i][0] = max(dp[i - 1][0], -p)
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + p)
        print(dp)
        return dp[-1][1]


class Solution2:
    def maxProfit(self, prices):
        buy, maxprofit = 0, 0
        for i in range(0, len(prices)):
            temp = max(prices[buy:])-prices[buy]
            if temp > maxprofit:
                maxprofit = temp
            if prices[i] < prices[buy]:
                buy = i
            else:
                continue
        return maxprofit


# Very Very brute force answer. My first answer :(
class Solution3:
    def maxProfit(self, prices):
        if not prices:
            return 0
        profit = 0
        buy_stock = prices[0]
        for i in range(len(prices)):
            if buy_stock > prices[i]:
                buy_stock = prices[i]
            profit = max((prices[i] - buy_stock, profit))
        return profit


    
a = Solution()
print(a.maxProfit([7,1,5,3,6,4]))
