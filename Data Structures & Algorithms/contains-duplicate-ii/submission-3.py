class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        ''' #hashmap solution- o(n) time, o(n) space
        mp = {}
        for i in range(len(nums)):
            if nums[i] in mp and i - mp[nums[i]] <= k:
                return True
            mp[nums[i]] = i
        return False '''

        # sliding window solution- here window is a hashset- shift when length exceeds k
        window = set()
        for i in range(len(nums)):
            if nums[i] in window:
                return True
            window.add(nums[i])
            if len(window) > k:
                window.remove(nums[i-k])
        return False
