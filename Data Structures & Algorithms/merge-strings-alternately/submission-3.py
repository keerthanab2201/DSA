class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i=0
        final=[] #creates empty list, not string-> join later
        while i<len(word1) or i<len(word2):
            if i<len(word1):
                final.append(word1[i]) #append() function can only be used for lists, not string
            if i<len(word2):
                final.append(word2[i])
            i+=1
        return "".join(final) #joins elements of list to form string

'''if we want to use strings- immutable in python so much slower but can be used in solution
final="" #or final=str()
final+=word1[i] #no append function, so use this operator
return final '''

        

