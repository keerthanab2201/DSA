class Solution:
    def isValid(self, s: str) -> bool:
        ''' approach- 
        when you see an opening bracket-> push it
        when you see a closing bracket-> (stack should not be empty, 
        TOS should be its matching opening bracket)-> pop it
        IMP- Inputs can be s = "()[]{}" or s = "([])", etc '''

        stack=[]
        mapping = { #keys are closing brackets, values are opening brackets
            ')': '(',
            '}': '{',
            ']': '['
        }
        for i in s:
            if i in "({[":
                stack.append(i)
            elif not stack or mapping[i]!=stack[-1]:
                return False
            else: 
                stack.pop()
        return not stack

