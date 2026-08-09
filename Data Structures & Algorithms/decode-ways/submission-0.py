class Solution:
    def numDecodings(self, s: str) -> int:
        # valid encodings are from 1 to 26
        # we have two choices at each position- take 1 digit or 2 consecutive digits=> ways("226")= ways("26")+ways("6")
        # cannot take two digits if it is >26
        # cannot take one digit if it is =0
        dp= [0]*(len(s)+1) # stores no of ways to decode string starting from i
        dp[len(s)]=1 #dummy base case-> string has been decoded successfully
        for i in range(len(s)-1,-1,-1):
            if s[i]=="0":
                dp[i]=0
            else:
                dp[i]= dp[i+1]
                if i+1<len(s) and (s[i]=="1" or (s[i]=="2" and s[i+1]<="6")):
                    dp[i]+=dp[i+2]
        return dp[0]
            
