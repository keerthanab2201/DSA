class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        ''' #hashmap solution- o(n) time, o(n) space
        mp = {}
        for i in range(len(nums)):
            if nums[i] in mp and i - mp[nums[i]] <= k:
                return True
            mp[nums[i]] = i
        return False '''

        # window size- lesser than or equal to k
        for i in range(len(nums)-1):
            j=i+1
            while j<len(nums) and abs(i-j)<=k:
                if nums[i]==nums[j]:
                    return True
                j+=1
        return False
