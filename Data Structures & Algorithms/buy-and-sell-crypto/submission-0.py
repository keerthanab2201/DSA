class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit=0
        minprice= prices[0]
        for i in range(len(prices)):
            minprice= min(prices[i],minprice)
            profit= prices[i]-minprice
            maxprofit= max(profit,maxprofit)
        return maxprofit