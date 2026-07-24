class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # no of outgoing edges= 0
        # no of incoming edges= n-1
        incoming= defaultdict(int)
        outgoing= defaultdict(int)
        for src,dest in trust:
            outgoing[src]+=1
            incoming[dest]+=1
        for i in range(1,n+1):
            if outgoing[i]==0 and incoming[i]==n-1:
                return i
        return -1