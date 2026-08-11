class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # we cannot use a 2 pointer approach since the word can be split in multiple ways
        # BU DP- start from end of string
        dp=[False]* (len(s)+1) # tells us whether s[i:] can be segmented
        # base case- empty string is valid
        dp[len(s)]=True
        for i in range(len(s)-1, -1, -1):
            for w in wordDict:
                if (i+len(w))<=len(s) and  s[i:i+len(w)]==w:
                    dp[i]= dp[i+len(w)]
                if dp[i]==True:
                    break
        return dp[0]
