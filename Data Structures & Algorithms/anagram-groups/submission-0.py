class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res= defaultdict(list)
        for s in strs:
            char= [0]*26 # initialise array to store count of all characters in string
            for c in s:
                char[ord(c)-ord('a')]+=1
            res[tuple(char)].append(s) 
            #To use character frequency arrays as keys, you must convert them to an immutable type (like a tuple)- makes it hashable
        return list(res.values())