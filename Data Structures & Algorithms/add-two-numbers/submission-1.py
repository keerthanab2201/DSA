# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #create new list to store result- DO NOT MODIFY
        carry=0
        dummy= ListNode() 
        curr= dummy
        while l1 or l2 or carry:
            curr.next = ListNode()
            curr = curr.next
            v1= l1.val if l1 else 0
            v2= l2.val if l2 else 0
            if v1+v2+carry>=10:
                curr.val = (v1+v2+carry)%10
                carry=1
            else:
                curr.val= v1+v2+carry
                carry=0
            if l1:
                l1= l1.next 
            if l2:
                l2= l2.next 
        return dummy.next 
       