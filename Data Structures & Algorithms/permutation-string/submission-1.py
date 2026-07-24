class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        # we use character array to count frequencies
        s1count= [0]*26 # has frequency count of the given string s1
        s2count= [0]*26 # this is the sliding window which will track frequency count of substrings in s2
        #first initialise both arrays
        for i in range(len(s1)):
            s1count[ord(s1[i])-ord('a')]+=1 #converts ascii value to scale of 0-26
            s2count[ord(s2[i])-ord('a')]+=1 #this will be initial position of sliding window
        # check first window
        if s1count==s2count:
            return True
        # else slide the window forward one character at a time
        for i in range(len(s1),len(s2)):
            s2count[ord(s2[i])-ord('a')]+=1 # add new char to array
            s2count[ord(s2[i-len(s1)])-ord('a')]-=1 # remove leftmost char from array
            if s1count==s2count: #compare arrays
                return True
        return False

        

        # sliding window must be exactly the length of s1

