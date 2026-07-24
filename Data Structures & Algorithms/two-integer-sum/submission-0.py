class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # iterate through array and check if difference exists as a number in hashmap
        hmap={} #maps number to its index
        for i in range(len(nums)):
            diff= target-nums[i]
            if diff in hmap:
                return [hmap[diff], i]
            hmap[nums[i]]= i


        