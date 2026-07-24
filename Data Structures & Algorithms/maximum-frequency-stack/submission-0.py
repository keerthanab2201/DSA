class FreqStack:
    
    def __init__(self):
        self.stacks = defaultdict(list) #dictionary of stacks: stacks[f] = all values that reached frequency f, in the order they reached it.
        self.counter= defaultdict(int)
        self.maxfreq=0

    def push(self, val: int) -> None:
        self.counter[val]+=1
        f= self.counter[val]
        self.maxfreq= max(self.maxfreq,f)
        self.stacks[f].append(val)
        
    def pop(self) -> int:
        val= self.stacks[self.maxfreq].pop()
        self.counter[val]-=1 #decrement count after popping
        if not self.stacks[self.maxfreq]: #if this maxfreq level has an empty list
            self.maxfreq-=1
        return val

        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()