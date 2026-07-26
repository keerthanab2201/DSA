class Solution:
    def climbStairs(self, n: int) -> int:
        # step i can be reached from step i-1 or step i-2
        # total ways to reach step i is sum of ways to reach previous two steps
        # fibonacci-like pattern
        if n<=2:
            return n
        dp= [0]*(n+1) # each element i of dp array stores no of ways to reach step i
        dp[1],dp[2]= 1,2 #initialise
        for i in range(3,n+1):
            dp[i]= dp[i-1]+dp[i-2]
        return dp[n]