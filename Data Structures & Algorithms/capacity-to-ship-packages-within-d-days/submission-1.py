class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        '''
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
            else:
                l=cap+1 #everything this small is impossible.
        return l # l is the smallest valid capacity '''

        l=max(weights)
        r=sum(weights)
        while l<=r:
            cap= l+ (r-l)//2
            d=1
            weight=0
            for i in weights:
                if i+weight<=cap:
                    weight+=i
                else:
                    d+=1
                    weight=i
            if d>days:
                l=cap+1
            else:
                r=cap-1
                res=cap
        return res
