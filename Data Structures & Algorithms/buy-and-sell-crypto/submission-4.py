class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        l = 0
        r = l

        for price in prices:
            profit = prices[r] - prices[l]
            maxProfit = max(profit, maxProfit)
            if prices[r] < prices[l]:
                l = r
            r = r + 1
        
        return maxProfit