class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1 #lower bound
        r= max(piles) #upper bound (max no of bananas to be eaten in one hour)
        while l<=r:
            k= l+(r-l)//2 # bananas per hour
            totaltime=0 # total time required to eat all bananas
            for i in piles:
                totaltime+= math.ceil(float(i)/k) #ceiling function rounds a decimal number up to the nearest integer
            if totaltime<=h:
                res=k
                r=k-1
            else:
                l=k+1
        return res

