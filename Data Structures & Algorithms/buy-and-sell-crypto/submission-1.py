class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit=0
        buy= prices[0]
        i=0
        while i<len(prices):
            if prices[i]<buy:
                buy=prices[i]
            else:
                profit= prices[i]-buy
                maxprofit= max(maxprofit,profit)
            i+=1
        return maxprofit

        
            
    