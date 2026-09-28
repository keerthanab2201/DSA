class ListNode:
    def __init__(self, key, val):
        self.key= key
        self.val= val
        self.freq=1
        self.prev=None
        self.next=None

class LinkedList:
    def __init__(self):
        self.head= ListNode(0,0)
        self.tail= ListNode(0,0)
        self.head.next= self.tail
        self.tail.prev= self.head
        self.size=0
    
    def insert(self, node):
    # node is inserted at end of newly updated frequency list (MRU)
        prv= self.tail.prev
        prv.next= node
        node.next= self.tail
        node.prev= prv
        self.tail.prev= node
        self.size+=1
    
    def remove(self, node):
    # removes node from its current frequency list
        node.prev.next= node.next
        node.next.prev= node.prev
        self.size-=1

    def removeLRU(self):
    # removes LRU node (at the beginning of linked list) when cache size reaches its capacity
        node= self.head.next
        self.remove(node)
        return node

class LFUCache:
    
    def __init__(self, capacity: int):
        self.capacity= capacity
        self.cache= {} # maps keys to nodes
        self.freqmap= defaultdict(LinkedList) # maps frequencies to doubly linked lists
        self.minfreq=0 # current minimum frequency
    
    def updatefreq(self,node):
        old= node.freq
        # remove node from old freq list
        self.freqmap[old].remove(node)
        # if old frequency list becomes empty
        if old==self.minfreq and self.freqmap[old].size==0:
            self.minfreq+=1
        # increase frequency and insert into new list
        node.freq+=1
        self.freqmap[node.freq].insert(node)

    def get(self, key):
        if key not in self.cache:
            return -1
        node= self.cache[key]
        self.updatefreq(node)
        return node.val
    
    def put(self, key, value):
        #if self.capacity == 0:
            #return
        if key in self.cache: # if key is already in cache then we just update its value
            node= self.cache[key]
            node.val= value
            self.updatefreq(node)
            return 
        if len(self.cache)==self.capacity: 
            lru= self.freqmap[self.minfreq].removeLRU()
            del self.cache[lru.key]
        # create a new node
        node= ListNode(key,value)
        self.cache[key]= node
        self.freqmap[1].insert(node)
        self.minfreq=1
        

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)