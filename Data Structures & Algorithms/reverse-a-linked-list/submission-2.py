# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev= None
        curr=head
        while curr:
            temp=curr.next #remembers where to go next
            curr.next=prev #flips arrow
            prev=curr #moves prev to next node
            curr=temp #moves curr to next node
        return prev
        
    
