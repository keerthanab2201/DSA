class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hm= defaultdict(int)
        for i in nums:
            hm[i]+=1
            if hm[i]> (len(nums)//2):
                return i
        