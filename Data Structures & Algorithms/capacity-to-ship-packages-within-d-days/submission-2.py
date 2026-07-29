class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        l= max(weights) #lower bound of ship capactiy is maximum weight of a package
        r= sum(weights) #upper bound can be sum of all packages' wrights
        while l<=r:
            cap= l+(r-l)//2
            daystaken=1
            load=0
            for i in weights:
                if load+i>cap:
                    daystaken+=1
                    load=i
                else:
                    load+=i
            if daystaken<=days:
                r=cap-1 #maybe an even smaller capacity also works
                res=cap
            else:
                l=cap+1 #everything this small is impossible.
        return res  

        