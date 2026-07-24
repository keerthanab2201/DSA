class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hm= defaultdict(int)
        for i in nums:
            if i in hm:
                hm[i]+=1
            else:
                hm[i]=1
        for j in hm:
            if hm[j]>1:
                return True
        return False #outside for loop- otherwise will return false prematurely and stop checking
