class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        res=0
        for i in tokens:
            if i not in "+-*/":
                stack.append(int(i))
            else: #ensure the top 2 items of stack are consumed and operated on
                b=stack.pop()
                a=stack.pop()
                if i=='+':
                    stack.append(a+b)
                elif i=='-':
                    stack.append(a-b)
                elif i=='*':
                    stack.append(a*b)
                else:
                    stack.append(int(a/b)) #truncates towards 0
        return stack[-1]