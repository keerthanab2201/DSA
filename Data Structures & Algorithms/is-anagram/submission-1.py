class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        hashs={}
        hasht={}
        for i in s:
            if i not in hashs:
                hashs[i]=1
            hashs[i]+=1
        for j in t:
            if j not in hasht:
                hasht[j]=1
            hasht[j]+=1
        return hashs==hasht
        
        