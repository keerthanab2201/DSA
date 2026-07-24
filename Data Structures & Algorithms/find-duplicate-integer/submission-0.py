class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''#use hash set- o(n) space or 
        #traverse input array itself- o(1) space- 
            #for every element go to the corresponding index and mark as negative- if already marked, it is a repeated number
        for i in nums:
            index= abs(i)-1
            if nums[index]<0:
                return abs(nums[index])
            nums[index]= -nums[index]'''

        '''alternate- floyds algorithm (slow and fast pointers)
        Treat the array like a linked list where each element points to the next element given by its val
        - slow pointer moves one step at a time.
        - fast pointer moves two steps at a time.
        - If there’s a cycle, they will eventually meet. '''
        slow=0
        fast=0
        while True:
            slow= nums[slow]
            fast= nums[nums[fast]]
            if slow==fast: 
                break
        '''but first meeting point is not guaranteed to be the duplicate
        The distance from start → cycle entrance = distance from meeting point → cycle entrance.
        If one pointer starts at the beginning and one starts at the meeting point, 
        and both move one step at a time, they will arrive at the entrance together '''
        slow2=0
        while True:
            slow=nums[slow]
            slow2=nums[slow2]
            if slow==slow2:
                return slow


