class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap= set()
        l=0
        r=0
        maxlen= 0
        for r in range(len(s)):
            while s[r] in hashmap:
                hashmap.remove(s[l])
                l+=1
            hashmap.add(s[r])
            maxlen=max(r-l+1,maxlen)
        return maxlen
