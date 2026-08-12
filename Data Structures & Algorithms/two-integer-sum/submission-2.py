class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # we use a hashmap to keep track of the numbers
        seen={}
        for i in range(len(nums)):
            diff= target-nums[i]
            if diff in seen:
                return [seen[diff],i]
            seen[nums[i]]=i




        