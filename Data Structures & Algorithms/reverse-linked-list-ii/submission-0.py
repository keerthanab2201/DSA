# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left==right:
            return head

        #IMP- create a dummy node pointing to head
        dummy= ListNode(0) 
        dummy.next= head

        # Move prev to the node before 'left' 
        prev= dummy
        for i in range(left-1):
            prev=prev.next

        curr= prev.next #curr now points to 'left' i.e, first node of sublist
        reversePrev= None #this new ptr disconnect sublist from left side
        tail= curr #after reversal, tail is the last node of sublist, curr will point to the node after that

        # Reverse the sublist- standard linked list reversal logic
        for i in range(right-left+1):
            temp= curr.next
            curr.next= reversePrev
            reversePrev=curr
            curr=temp

        # now reconnect
        prev.next= reversePrev
        tail.next= curr

        return dummy.next

        
