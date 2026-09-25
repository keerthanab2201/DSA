class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
    # optimal sliding window soln: 
    # replacements needed = len(window) - freq of most common character
        l=r=0
        count= defaultdict(int) # hashmap stores freq of each char in the current window
        maxfreq=0 # stores most common char in current window- this is what we can replace other chars with for minimum replaements
        maxlen=0
    
        while r<len(s):
            count[s[r]]+=1
            maxfreq= max(maxfreq, count[s[r]])
            while (r-l+1)-maxfreq>k: # invalid window
                count[s[l]]-=1
                l+=1
            maxlen= max(maxlen, r-l+1)
            r+=1
        return maxlen 


            



