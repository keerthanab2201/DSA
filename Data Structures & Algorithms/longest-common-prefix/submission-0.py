class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        seen= list(strs[0])
        for s in strs:
            i=0
            while i<len(s) and i<len(seen) and s[i]==seen[i]:
                i+=1
            seen= seen[0:i]
        return "".join(seen)
