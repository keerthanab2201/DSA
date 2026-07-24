# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    '''def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    # iteratively merge pairs of lists- o(k*n) not optimal
        if len(lists)==0:
            return None
        for i in range(len(lists)-1,0,-1):
            lists[i-1]= self.mergeTwoLists(lists[i], lists[i-1])
        return lists[0]

    def mergeTwoLists(self, l1, l2):
            dummy= ListNode()
            curr= dummy
            while l1 and l2:
                if l1.val<l2.val:
                    curr.next=l1
                    l1= l1.next
                else:
                    curr.next=l2
                    l2=l2.next
                curr=curr.next
            curr.next= l1 if l1 else l2
            return dummy.next '''
    
    #optimal soln- min heap(priority queue)- o(nlogk)
    # this always picks smallest current node among all k lists- no need to scan all heads every time

    def mergeKLists(self, lists:List[Optional[ListNode]])->Optional[ListNode]:
        minheap=[]
        res= ListNode(0)
        # push first node of each list into heap
        for i,node in enumerate(lists):
            if node:
                heapq.heappush(minheap,(node.val,i,node)) #we store all 3 things- if two values are equal, index is compared
        # create answer list
        dummy= ListNode(0)
        curr=dummy
        while minheap:
            value,i,node= heapq.heappop(minheap) #pop the smallest value node
            curr.next= node #appends the popped node to new linked list
            curr= curr.next #move ptr forward
            if node.next: #after popping the node, we push the next node of that list onto heap
                heapq.heappush(minheap, (node.next.val,i,node.next))
        return dummy.next



        