# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # split= before group | group of k nodes | remaining list
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy= ListNode(0)
        dummy.next=head
        groupprev=dummy
        while True:
            kthnode= self.getkth(groupprev,k)
            if not kthnode:
                break
            groupnext= kthnode.next
            groupstart= groupprev.next
            curr= groupstart
            prev= groupnext #IMP
            while curr!= groupnext:
                temp= curr.next
                curr.next= prev
                prev= curr
                curr= temp
            groupprev.next= kthnode #start of reversed group
            groupprev= groupstart
        return dummy.next 

    def getkth(self, curr:Optional[ListNode], k:int)-> Optional[ListNode]:
        for i in range(k):
            if not curr:
                break
            curr=curr.next
        return curr

        