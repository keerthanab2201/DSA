class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap= set()
        if not s:
            return 0
        l=0
        r=0
        maxlen= 1
        while r<len(s):
            if s[r] not in hashmap: #encounter new char that is not repeated in window
                hashmap.add(s[r]) # add to hashset 
                maxlen= max(maxlen,r-l+1) #compute length of window. check if it is max
                r+=1 #move right pointer forward by 1
            else: #encounter a char that is already present in the window
                hashmap.remove(s[l]) #remove the current left pointer from hashset
                l+=1 #move the left pointer forward by 1
        return maxlen
        


