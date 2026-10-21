class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        # champion- no of incoming edges=0
        incoming =[0]*n
        for u,v in edges:
            incoming[v]+=1
        champions=[]
        for node,incomingedges in enumerate(incoming):
            if incomingedges==0:
                champions.append(node)
        return -1 if len(champions)>1 else champions[0]



