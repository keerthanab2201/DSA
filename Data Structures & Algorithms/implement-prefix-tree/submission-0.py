class TrieNode:
    def __init__(self):
        self.children= [None]*26 #we use a character array that stores children for each node
        self.endofword= False #boolean that marks end of word
    
class PrefixTree:

    def __init__(self):
        self.root= TrieNode() #starting node- doesnt hold ay character

    def insert(self, word: str) -> None:
        curr= self.root
        for char in word: #here char needs to be converted to index in range 0-25 to search in the array
            i= ord(char)-ord('a')
            if not curr.children[i]:
                curr.children[i]= TrieNode()
            curr= curr.children[i]
        curr.endofword=True
            
    def search(self, word: str) -> bool:
        curr= self.root
        for char in word:
            i= ord(char)-ord('a')
            if not curr.children[i]:
                return False
            curr=curr.children[i]
        return curr.endofword
            
    def startsWith(self, prefix: str) -> bool:
        curr= self.root
        for char in prefix:
            i= ord(char)-ord('a')
            if not curr.children[i]:
                return False
            curr=curr.children[i]
        return True
        
        