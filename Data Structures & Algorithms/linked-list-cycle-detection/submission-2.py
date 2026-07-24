# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''naive solution- hashset- o(1)time and o(n)space
        curr=head
        visited=set()
        while curr:
            if curr not in visited:
                visited.add(curr)
            else:
                return True
            curr= curr.next
        return False'''
        # slow and fast pointers- IMP
        slow= head #moves one step
        fast= head #moves two steps
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False



