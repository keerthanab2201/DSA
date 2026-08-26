class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
       # for a list to be sorted, adjacent words should be in correct order
       cmap= {c:i for i,c in enumerate(order)}
       for i in range(len(words)-1):
        w1=words[i]
        w2=words[i+1]
        for j in range(min(len(w1),len(w2))):
            if cmap[w1[j]]>cmap[w2[j]]:
                return False
            elif cmap[w1[j]]<cmap[w2[j]]:
                break # we dont need to compare rest of characters if first ones are already lexically sorted- think about how a dictionary works
        # now all characters of shorter word are matched
        else:
            if len(w1)>len(w2):
                return False
       return True
