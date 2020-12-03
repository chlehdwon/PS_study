# Say you have an array for which the ith element is the price of
# a given stock on day i.

# If you were only permitted to complete at most one transaction
# (i.e., buy one and sell one share of the stock),
# design an algorithm to find the maximum profit.

# Note that you cannot sell a stock before you buy one.


class Solution:
    def maxProfit(self, prices):
        buy, maxprofit = 0, 0
        for i in range(0, len(prices)):
            if prices[i] < buy:
                buy = i
            else:
                continue
            temp = max(prices[buy:])-prices[buy]
            if temp > maxprofit:
                maxprofit = temp
        return maxprofit


a = Solution()
print(a.maxProfit([7,1,5,3,6,4]))
