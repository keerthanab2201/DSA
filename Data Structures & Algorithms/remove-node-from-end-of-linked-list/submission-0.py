# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #nth node from the end is [len(list)-n]th node
        curr=head
        len=0
        while curr:
            curr=curr.next
            len+=1
        removeindex= len-n
        if removeindex==0:
            return head.next
        curr=head
        k=0
        while k<removeindex-1:
            curr=curr.next
            k+=1
        curr.next=curr.next.next
        return head

