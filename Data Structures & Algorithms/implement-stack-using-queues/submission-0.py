class MyStack:
    # STACK- LIFO, QUEUE- FIFO
    #use 2 queues- when pushing a new element, we add it to the empty second queue, then move all elements from the first queue behind it. 
    def __init__(self):
        self.q1= deque() #initialise double ended queue
        self.q2= deque()

    def push(self, x: int) -> None:
        self.q2.append(x) #append new element to empty queue
        while self.q1: #transfer elements from q1 to q2
            y= self.q1.popleft() # pops element from front of queue
            self.q2.append(y)
        self.q1, self.q2= self.q2, self.q1 #ensures q1 has all elements 
        
    def pop(self) -> int:
        return self.q1.popleft()
        
    def top(self) -> int:
        return self.q1[0]
        
    def empty(self) -> bool:
        if len(self.q1)==0:
            return True
        return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()