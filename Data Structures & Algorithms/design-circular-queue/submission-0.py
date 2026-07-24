class ListNode:
    def __init__(self, val, next=None):
        self.val=val
        self.next= next

class MyCircularQueue: #circular singly linked list

    def __init__(self, k: int):
        self.space= k #this keeps track of how much space is remaining in LL
        self.dummy= ListNode(0) #dummy node points to head
        self.tail= self.dummy #tail will point to last node in LL

    def enQueue(self, value: int) -> bool:
        if self.isFull(): #cannot insert new node if LL is full
            return False
        curr= ListNode(value) # create a new node with given value
        if self.isEmpty(): #if LL is empty, new node becomes the head&tail
            self.dummy.next= curr
            self.tail= curr
        else: #else insert new node after tail
            self.tail.next= curr
            self.tail= curr
        self.space-=1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.dummy.next= self.dummy.next.next
        self.space+=1
        return True
        

    def Front(self) -> int:
        if not self.dummy.next:
            return -1
        return self.dummy.next.val

    def Rear(self) -> int:
        if not self.dummy.next:
            return -1
        return self.tail.val
        
    def isEmpty(self) -> bool:
        if not self.dummy.next:
            return True
        return False

    def isFull(self) -> bool:
        if self.space==0:
            return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()