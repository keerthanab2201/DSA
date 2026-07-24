class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split("/")
        stack = []
        for cur in paths:
            if cur == "..": #this condition should be checked first seperate from stack otherwise elif condition will be true
                if stack: 
                    stack.pop()
            elif cur != "" and cur != ".":
                stack.append(cur)

        return "/" + "/".join(stack)