
class Node:
    def __init__(self, key, val):
        self.key=key
        self.val=val
        self.prev= self.next= None
       
class LRUCache:
# doubly linked list- helps keep track of order- least recently used is at head, most recently used is at the tail
# hashmap- efficient o(1) retrieval
    def __init__(self, capacity: int):
        self.cache= {} #dictionary maps key to NODES 
        self.capacity=capacity
        #create two dummy nodes for DLL- all nodes to be inserted/removed in between these two
        self.left= Node(0,0)
        self.right= Node(0,0)
        self.left.next= self.right
        self.right.prev= self.left
    
    def remove(self,node): # func to remove a node
        prv= node.prev
        nxt= node.next
        prv.next= nxt
        nxt.prev= prv

    def insert(self,node): # func to insert new node at the end of DLL (before dummy right)
        prv= self.right.prev
        nxt= self.right
        prv.next= nxt.prev= node #first assign to neighbours
        node.prev= prv
        node.next= nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            node= self.cache[key]
            self.remove(node) #remove node from its position in DLL
            self.insert(node) #insert node at the end
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key]) #remove node from its position in DLL
        self.cache[key]= Node(key,value) # update its value in cache
        self.insert(self.cache[key]) #insert node at end of DLL
        if len(self.cache)>self.capacity:
            lru= self.left.next 
            self.remove(lru) #remove lru node (node after dummy left)
            del self.cache[lru.key] 



