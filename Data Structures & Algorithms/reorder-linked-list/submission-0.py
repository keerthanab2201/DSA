# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find middle of linked list- using fast and slow pointers
        #when fast reaches the end, slow reaches midpoint
        slow= head
        fast= head.next #imp
        while fast and fast.next:
            slow= slow.next
            fast= fast.next.next

        #reverse the second half of the list
        second= slow.next
        prev = slow.next = None #breaks list into two halves
        while second:
            temp= second.next
            second.next= prev
            prev= second
            second= temp
        
        first= head # first node of first half
        second= prev #this now points to first node of second half
        while second:
            temp1= first.next 
            temp2= second.next
            first.next= second 
            second.next= temp1
            first= temp1
            second= temp2



