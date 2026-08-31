class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # this is a state machine DP
        # there are 3 possible states- holding, not holding + can buy, not holding + cooldown
        '''hold[i] = maximum profit on day i while holding a coin
        canbuy[i] = maximum profit on day i while NOT holding and allowed to buy
        cooldown[i] = maximum profit on day i while NOT holding and in the cooldown period'''
        ''' State transitions: 
        FREE ──buy──> HOLD
        FREE ──stay─> FREE
        HOLD ──stay─> HOLD
        HOLD ──sell─> COOLDOWN
        COOLDOWN ──next day──> FREE '''
        hold= -prices[0] # On day 0, the only way to be holding a coin is to buy it-> profit is negative
        canbuy= 0
        cool= 0
        for i in range(1,len(prices)):
            prevhold= hold
            prevcanbuy= canbuy
            prevcool= cool
            hold= max(prevhold, prevcanbuy-prices[i]) # ways to reach hold state 
            cool= prevhold+prices[i]
            canbuy= max(prevcanbuy, prevcool)
        return max(canbuy,cool)
